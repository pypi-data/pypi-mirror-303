import multiprocessing
import atexit
import numpy as np
from threading import Thread
from functools import wraps
import traceback
from _queue import Empty
import os
from contextlib import contextmanager
import sys
import inspect
from multiclass_interface.multi_object_list import MultiObjectList


def run(cls, inputQueue, outputQueue, cls_args, **kwargs):
    o = cls(*cls_args, **kwargs)
    while True:
        method, args, kwargs = inputQueue.get()
        try:
            if method == 'getattr':
                name = args[0]
                outputQueue.put(getattr(o, name))
            elif method == 'setattr':
                name, value = args
                if hasattr(value, '__call__'):  # pragma: no cover # cov not registered?

                    def wrap(*args, func=value, **kwargs):
                        if inspect.getfullargspec(func).args[:1] == ['self']:
                            args = (o,) + args
                        return func(*args, **kwargs)
                    value = wrap
                outputQueue.put(setattr(o, name, value))
            elif method == 'iscallable':
                name = args[0]
                outputQueue.put(hasattr(getattr(o, name), '__call__'))
            else:
                att = getattr(o, method)
                outputQueue.put(att(*args, **kwargs))
        except BaseException as e:
            outputQueue.put((e, traceback.format_exc()))
        finally:
            if method == 'close':
                outputQueue.put('Exit process')
                return


class ProcessClass():
    cls = None

    def __init__(self, cls, cls_attrs={}, index=""):
        self.cls_attrs = cls_attrs
        self.index = index
        self.cls = cls
        self.ctx = multiprocessing.get_context('spawn')
        self.inputQueue = self.ctx.Queue()
        self.outputQueue = self.ctx.Queue()
        atexit.register(self.close)
        self.closed = False

    def __call__(self, *args, **kwargs):
        kwargs.update({'cls': self.cls, 'inputQueue': self.inputQueue, 'outputQueue': self.outputQueue,
                       'cls_args': args})
        s = 'vs_debug.py'
        if s in "".join(traceback.format_stack()):  # pragma: no cover
            self.process = Thread(target=run, kwargs=kwargs)  # use this to debug from Visual studio
        else:
            self.process = self.ctx.Process(target=run, kwargs=kwargs, daemon=True)

        self.process.start()
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __getattribute__(self, name):
        try:
            if name != 'cls_attrs' and name in self.cls_attrs:
                raise AttributeError()
            return object.__getattribute__(self, name)
        except AttributeError:
            return self.getattr(name, None)

    def getattr(self, name, is_callable):
        if is_callable is None:
            is_callable = self.is_callable(name)
        if is_callable:
            @wraps(getattr(self.cls, name, None))
            def wrap(*args, wait_for_result=True, **kwargs):
                self.inputQueue.put((name, args, kwargs))
                if wait_for_result:
                    return self.get_result(
                        raise_exception=True,
                        cmd=lambda: f'executing {name}({", ".join(list(map(str, args)) + ["%s=%s" % (k, v) for k, v in kwargs.items()])})')
            return wrap
        else:
            self.inputQueue.put(('getattr', (name,), {}))
            return self.get_result(raise_exception=True, cmd=lambda: f"getting attribute '{name}'")

    def is_callable(self, name):
        self.inputQueue.put(('iscallable', (name,), {}))
        return self.get_result(raise_exception=True, cmd=lambda: f"checking if '{name}' is callable")

    def __setattr__(self, name, value):
        if name in {'cls', 'ctx', 'inputQueue', 'outputQueue', 'closed', 'process', 'cls_attrs', 'index'}:
            return object.__setattr__(self, name, value)
        else:
            self.inputQueue.put(('setattr', (name, value), {}))
            return self.get_result(raise_exception=True, cmd=lambda: f"setting attribute '{name}'")

    def get_result(self, raise_exception, cmd):
        while True:
            if self.process.is_alive() or self.closed:
                try:
                    res = self.outputQueue.get(timeout=2)
                    if isinstance(res, tuple) and len(res) > 1 and isinstance(res[0], BaseException):
                        res = res[0].__class__(res[1])
                        if raise_exception:
                            raise res
                    return res
                except Empty:
                    pass  # time out. Check process is alive and try again
            else:
                if hasattr(cmd, '__call__'):
                    cmd = cmd()
                p_id = f'{self.cls.__name__} process'
                if self.index:
                    p_id += f" index {self.index}"
                e = Exception(f'{p_id} died before or while {cmd}')
                if raise_exception:
                    raise e
                return e

    def close(self, wait_for_result=False):
        if not self.closed:
            self.inputQueue.put(('close', [], {}))
            r = self.get_result(False, 'close')
            self.get_result(False, 'get process exit message')
            self.process.join()
            self.inputQueue.close()
            self.outputQueue.close()
            self.closed = True
            return r


class ThreadClass(ProcessClass):
    def __call__(self, *args, **kwargs):
        kwargs.update({'cls': self.cls, 'inputQueue': self.inputQueue, 'outputQueue': self.outputQueue,
                       'cls_args': args})
        self.process = Thread(target=run, kwargs=kwargs)  # use this to debug from Visual studio
        self.process.start()
        return self


class MultiProcessClassInterface(MultiObjectList):

    def __init__(self, cls, args_lst, cls_attrs={}):
        MultiObjectList.__init__(self, [ProcessClass(cls, cls_attrs, i)(*args)
                                 for i, args in enumerate(args_lst)], SubsetProcessWrapper)

    def __getattr__(self, name):
        obj_lst = self.obj_lst
        if obj_lst[0].is_callable(name):
            def wrap(*args, **kwargs):
                for obj, (o_args, o_kwargs) in zip(obj_lst, self.get_obj_args_lst(args, kwargs)):
                    obj.getattr(name, True)(*o_args, wait_for_result=False, **o_kwargs)
                res = [o.get_result(raise_exception=False, cmd=lambda: f"executing {name}(...)")
                       for o in obj_lst]
                for r in res:
                    if isinstance(r, Exception):
                        raise r
                return res
            return wrap
        else:
            return [o.getattr(name, False) for o in obj_lst]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self, wait_for_result=False):
        for obj in self.obj_lst:
            obj.close()
            # if not obj.closed:
            #     obj.inputQueue.put(('close', [], {}))
            #     obj.process.join()
            #     obj.closed = True


class MultiThreadClassInterface(MultiProcessClassInterface):
    def __init__(self, cls, args_lst, cls_attrs={}):
        MultiObjectList.__init__(self, [ThreadClass(cls, cls_attrs)(*args) for args in args_lst], SubsetProcessWrapper)


class SubsetProcessWrapper(MultiProcessClassInterface):
    def __init__(self, obj_lst):
        MultiObjectList.__init__(self, obj_lst)

    def __getitem__(self, slice):
        if np.all(np.atleast_1d(self.obj_lst[slice]) == self.obj_lst):
            return self
        raise Exception('Cannot make subset of SubsetProcessWrapper')

    def __getattribute__(self, name):
        if name == 'close':
            raise Exception("Cannot close SubsetProcessWrapper. Please close all instances at once")

        return MultiProcessClassInterface.__getattribute__(self, name)

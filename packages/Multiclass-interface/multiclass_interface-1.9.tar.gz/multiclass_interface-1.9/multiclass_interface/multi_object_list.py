import numpy as np


class MultiObjectList():
    def __init__(self, obj_lst, subset_cls=None):
        self.obj_lst = np.atleast_1d(obj_lst)
        self.subset_cls = subset_cls

    def __str__(self):
        return f'{self.__class__.__name__}({self.obj_lst})'

    def get_obj_args_lst(self, args, kwargs):
        N = len(self.obj_lst)

        def get_obj_args(i):
            def get_arg(arg):
                if isinstance(arg, list) and len(arg) == N:
                    return arg[i]
                else:
                    return arg
            obj_args = [get_arg(arg) for arg in args]
            obj_kwargs = {k: get_arg(v) for k, v in kwargs.items()}
            return obj_args, obj_kwargs
        return [get_obj_args(i) for i in range(N)]

    def iscallable(self, name):
        return hasattr(getattr(self.obj_lst[0], name), '__call__')

    def __getitem__(self, s):
        obj_lst = np.atleast_1d(self.obj_lst[s])
        if len(obj_lst) == len(self.obj_lst) and np.all(obj_lst == self.obj_lst):
            return self
        subset_cls = self.subset_cls or MultiObjectList
        return subset_cls(self.obj_lst[s])

    def __getattr__(self, name):
        att_lst = [getattr(obj, name) for obj in self.obj_lst]
        if self.iscallable(name):
            def wrap(*args, **kwargs):
                return [att(*o_args, **o_kwargs)
                        for att, (o_args, o_kwargs) in zip(att_lst, self.get_obj_args_lst(args, kwargs))]
            return wrap
        else:
            return att_lst

    def __setattr__(self, name, value):
        if name in {'obj_lst', 'subset_cls', 'cls'}:
            return object.__setattr__(self, name, value)
        obj_lst = self.obj_lst
        for obj, (o_args, _) in zip(obj_lst, self.get_obj_args_lst((value,), {})):
            setattr(obj, name, *o_args)


class MultiClassInterface(MultiObjectList):
    def __init__(self, cls, args_lst):
        self.cls = cls
        MultiObjectList.__init__(self, [cls(*args) for args in args_lst])

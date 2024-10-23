from numpy import testing as npt
import pytest

from multiclass_interface.multiprocess_interface import MultiProcessClassInterface, MultiThreadClassInterface, \
    ProcessClass
from multiclass_interface.tests.my_test_cls import MyTest
from threading import Thread


@pytest.fixture(scope='module')
def mpri():
    with MultiProcessClassInterface(MyTest, [(1,), (2,), (3,)]) as mpri:
        yield mpri


@pytest.fixture(scope='module')
def mthi():
    with MultiThreadClassInterface(MyTest, [(1,), (2,)]) as mthi:
        yield mthi


def test_attribute(mpri):
    npt.assert_array_equal(mpri.get_id(), [1, 2, 3])
    npt.assert_array_equal(mpri.name, ["MyTest1", "MyTest2", "MyTest3"])
    assert mpri[1].get_id() == [2]


def test_missing_attribute(mpri):
    with pytest.raises(AttributeError, match="'MyTest' object has no attribute 'missing'"):
        print(mpri.missing)


def test_execption(mpri):
    with pytest.raises(ZeroDivisionError, match="1 / 0  # raise ZeroDivisionError"):
        mpri.raise_exception()


def test_setattr(mpri):
    mpri.my_att = "new attribute"
    npt.assert_array_equal(mpri.my_att, ['new attribute'] * 3)


def get_process_id():
    import os
    return os.getpid()


def test_setattr_method(mpri):
    mpri.get_process_id = get_process_id
    main_id = get_process_id()
    pid1, pid2, pid3 = mpri.get_process_id()
    if isinstance(mpri, MultiProcessClassInterface):
        assert len({main_id, pid1, pid2, pid3}) == 4  # process ids should be unique
    else:
        # mpi, rank0 = main and first worker
        assert main_id == pid1
        assert pid1 != pid2
        assert pid2 != pid3


def test_str(mpri):
    assert str(mpri).startswith(
        'MultiProcessClassInterface([<multiclass_interface.multiprocess_interface.ProcessClass object at ')


def test_subset(mpri):
    assert mpri[1][:].get_id() == [2]
    with pytest.raises(Exception, match="Cannot make subset of SubsetProcessWrapper"):
        mpri[:2][0]

    with pytest.raises(Exception, match="Cannot close SubsetProcessWrapper. Please close all instances at once"):
        mpri[1].close()


@pytest.mark.parametrize('index,s', [('', ''), (5, ' index 5')])
def test_dying_process(index, s):
    pri = ProcessClass(MyTest, index=index)(1)

    def run():
        with pytest.raises(Exception, match=f"MyTest process{s} died before or while checking if 'work' is callable"):
            pri.work(5)
    t = Thread(target=run)
    t.start()
    pri.process.kill()
    t.join()


def test_MultiThreadClassInterface_attribute(mthi):
    npt.assert_array_equal(mthi.get_id(), [1, 2])
    npt.assert_array_equal(mthi.name, ["MyTest1", "MyTest2"])


def test_MultiThreadClassInterface_setattr(mthi):
    mthi.my_att = "new attribute"
    npt.assert_array_equal(mthi.my_att, ['new attribute'] * 2)


def test_process_class():
    with ProcessClass(MyTest, {'name'})(1) as pc:
        assert pc.name == "MyTest1"
        assert pc.get_id() == 1
        pc.work(3)
        with pytest.raises(ZeroDivisionError):
            pc.raise_exception()

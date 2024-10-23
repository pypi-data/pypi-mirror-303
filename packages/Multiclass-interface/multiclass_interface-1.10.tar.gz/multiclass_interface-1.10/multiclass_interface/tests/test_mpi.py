import os
import time

from numpy import testing as npt
import pytest

from multiclass_interface.mpi_interface import MPIClassInterface
from multiclass_interface.multiprocess_interface import ProcessClass, MultiProcessClassInterface
import numpy as np
from multiclass_interface.tests.my_test_cls import MyTest
from multiclass_interface import mpi_interface


def mpitest_mpi_MyTest():

    N = 4
    try:
        with MPIClassInterface(MyTest, [(i,) for i in range(N)]) as m:

            time.sleep(.1)
            i = m.get_id()
            npt.assert_array_equal(i, np.arange(N))

            npt.assert_array_equal(m[1:3].get_id(), np.arange(1, 3))
            t = time.time()
            m.work(1)
            t = time.time() - t
            assert t < 1.1

            with pytest.raises(Exception, match='Cannot close SubsetMPIClassInterface. Please close all instances at once'):
                m[:3].close()
            with pytest.raises(Exception, match='Cannot make subset of SubsetMPIClassInterface'):
                m[:3][1]

            print("done, test_mpi_MyTest")
    except ChildProcessError:
        pass


def mpitest_mpi_ProcessClass():

    with ProcessClass(MyTest) as cls:
        myTest = cls(1)
        assert myTest.get_id() == 1
    print("done, test_mpi_ProcessClass", flush=True)


def mpitest_non_collective_mpi():
    mpi_interface.COLLECTIVE_MPI = False
    rank = mpi_interface.rank
    import time
    N = 3
    with MPIClassInterface(MyTest, [(i + 10,) for i in range(N)]) as m:

        try:
            assert m.get_id()[0] == rank + 10, m.get_id()
            assert rank < N  # rank > N will fail with ChildProcessError
        except ChildProcessError:
            pass

    mpi_interface.COLLECTIVE_MPI = True


def mpitest_all():
    mpi_interface.activate_mpi()

    mpi_interface.exit_mpi_on_close = False
    rank = mpi_interface.rank
    from multiclass_interface.tests.test_multiprocessinterface import test_attribute, test_missing_attribute, test_execption, test_setattr, test_setattr_method
    mpi_interface.TERMINATE_ON_CLOSE = False

    def run(f, *args):
        try:
            if rank == 0:
                print(f"Rank {rank} start {f.__name__}", flush=True)
            f(*args)
        except ChildProcessError:
            pass
        finally:
            if rank == 0:
                print(f"Rank {rank} done {f.__name__}", flush=True)
    for f in [mpitest_mpi_MyTest,
              mpitest_mpi_ProcessClass]:
        run(f)

    try:
        with MPIClassInterface(MyTest, [(1,), (2,), (3,)]) as mpici:
            for f in [test_attribute, test_missing_attribute, test_execption, test_setattr, test_setattr_method]:

                run(f, mpici)

    except ChildProcessError:
        pass

    run(mpitest_non_collective_mpi)

    print(f"Rank {rank} Done test_all")

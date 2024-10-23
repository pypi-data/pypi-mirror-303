from multiclass_interface.multi_object_list import MultiClassInterface
from multiclass_interface.tests.my_test_cls import MyTest


def test_multiobject_list():
    multi_lst = MultiClassInterface(MyTest, [(i,) for i in [0, 1, 2]])
    assert multi_lst.get_id() == [0, 1, 2]

    assert multi_lst.return_input([3, 2, 1]) == ['0 got: (3,) and {}', '1 got: (2,) and {}', '2 got: (1,) and {}']

    assert multi_lst[1].get_id() == [1]
    assert multi_lst[:].get_id() == [0, 1, 2]

    assert multi_lst.id == [0, 1, 2]

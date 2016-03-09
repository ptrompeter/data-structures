# _*_ coding: utf-8 _*_


def test_dll_insert():
    from double_linked_list import Dbl_list
    from linked_list import Node
    from linked_list import LinkedList
    test_list = Dbl_list(['mom', '32', 43, [1,2]])
    test_list.insert(3)
    assert test_list.head.data == 3



def test_dll_append():
    pass

def test_dll_pop():
    from double_linked_list import Dbl_list
    test_list = Dbl_list(['mom', '32', 43, [1,2]]) 
    head = test_list.head
    assert test_list.pop() == head.data

def test_dll_shift():
    pass

def test_dll_remove():
    pass
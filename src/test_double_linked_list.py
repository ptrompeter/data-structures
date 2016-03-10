# _*_ coding: utf-8 _*_
import pytest

def test_dll_insert():
    from double_linked_list import Dbl_list
    from linked_list import Node
    from linked_list import LinkedList
    test_list = Dbl_list(['mom', '32', 43, [1,2]])
    test_list.insert(3)
    assert test_list.head.data == 3



def test_dll_append():
    from double_linked_list import Dbl_list
    test_list = Dbl_list(['mom', '32', 43, [1,2]])
    test_list.append(3)
    assert test_list.tail.data == 3

def test_dll_pop():
    from double_linked_list import Dbl_list
    test_list = Dbl_list(['mom', '32', 43, [1,2]]) 
    head = test_list.head
    assert test_list.pop() == head.data

def test_dll_shift():
    from double_linked_list import Dbl_list
    test_list = Dbl_list(['mom', '32', 43, [1,2]]) 
    tail = test_list.tail
    assert test_list.shift() == tail.data

def test_dll_remove():
    from double_linked_list import Dbl_list
    this_list = Dbl_list([1])
    this_list.insert(2)
    this_list.insert(4)
    this_list.insert('bob')
    search = this_list.search(4)
    this_list.remove(search)
    #assert this_list.search(4) == None
    assert this_list.size() == 3

def test_dll_remove2():
    from double_linked_list import Dbl_list
    this_list = Dbl_list([1])
    search = this_list.search(4)
    with pytest.raises(AttributeError):
        this_list.remove(search)

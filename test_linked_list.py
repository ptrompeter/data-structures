# _*_ coding: utf-8 _*_
import pytest


VAL_LIST = [
    [2, 3, 4],
    [4, 2, 3],
    ['test', 'makes', 'angry'],
    [(6, 6)],
]


def test_LinkedList():
    from linked_list import LinkedList
    assert type(LinkedList) == type


def test_LinkedList_2():
    from linked_list import LinkedList
    test_empty = LinkedList()
    assert test_empty.values == []


@pytest.mark.parametrize('a', VAL_LIST)
def test_LinkedList_3(a):
    from linked_list import LinkedList
    test_values = LinkedList([a])
    assert test_values.values == [a]


@pytest.mark.parametrize('a', VAL_LIST)
def test_LinkedList_4(a):
    from linked_list import LinkedList
    test_values = LinkedList([a])
    assert test_values.display() == 

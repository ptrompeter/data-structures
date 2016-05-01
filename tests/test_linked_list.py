# _*_ coding: utf-8 _*_
import pytest
from src.linked_list import LinkedList


VAL_LIST = [
    ([2, 3, 4], "(4, 3, 2,)"),
    ([4, 2, 3], "(3, 2, 4,)"),
    (['test', 'makes', 'angry'], "('angry', 'makes', 'test',)"),
]

SINGLE_VAL = [
    ([3]),
    (['peach']),
    ([(4, 5)]),
]


def test_LinkedList():
    assert type(LinkedList) == type


def test_LinkedList_2():
    test_empty = LinkedList()
    assert test_empty.values == []


@pytest.mark.parametrize('a', VAL_LIST)
def test_LinkedList_3(a):
    test_values = LinkedList(a)
    assert test_values.values == a


@pytest.mark.parametrize('a, b', VAL_LIST)
def test_LinkedList_4(a, b):
    test_values = LinkedList(a)
    assert test_values.display() == b


@pytest.mark.parametrize('a', SINGLE_VAL)
def test_LinkedList_insert(a):
    this_list = LinkedList([1])
    this_list.insert(a)
    assert this_list.head.data == a


@pytest.mark.parametrize('a', VAL_LIST)
def test_LinkedList_size(a):
    test_values = LinkedList(a)
    assert test_values.size() == len(a)


@pytest.mark.parametrize('a', VAL_LIST)
def test_LinkedList_search(a):
    test_values = LinkedList(a)
    assert test_values.search(test_values.head.data) == test_values.head


@pytest.mark.parametrize('a', SINGLE_VAL)
def test_LinkedList_remove_2(a):
    this_list = LinkedList(a)
    this_list.remove(this_list.head)
    assert this_list.size() == 0


def test_remove_one():
    lst = LinkedList([x for x in xrange(10)])
    node = lst.head.next_node.next_node
    lst.remove(node)
    assert lst.size() == 9


def test_display():
    lst = LinkedList([x for x in xrange(10)])
    assert lst.display() == "(9, 8, 7, 6, 5, 4, 3, 2, 1, 0,)"


def test_display2():
    lst = LinkedList(['foo', 'sarah'])
    assert lst.display() == "('sarah', 'foo',)"




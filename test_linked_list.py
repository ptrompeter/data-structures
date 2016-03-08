# _*_ coding: utf-8 _*_
import pytest


VAL_LIST = [
    ([2, 3, 4], ["(4, 3, 2)"]),
    ([4, 2, 3], ["(3, 2, 4)"]),
    (['test', 'makes', 'angry'], ["('angry', 'makes', 'test')"]),
]

SINGLE_VAL = [
    (3),
    ('peach'),
    ((4, 5)),
    (True),
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


@pytest.mark.parametrize('a, b', VAL_LIST)
def test_LinkedList_4(a, b):
    from linked_list import LinkedList
    test_values = LinkedList([a])
    assert test_values.display() == b


def test_LinkedList_remove():
    from linked_list import LinkedList
    this_list = LinkedList([1])
    this_list.remove(this_list.search(1))
    assert this_list.size() == 0


def test_LinkedList_remove_2():
    from linked_list import LinkedList
    this_list = LinkedList([1])
    this_list.remove(this_list.head)
    assert this_list.size() == 0


@pytest.mark.parametrize('a', SINGLE_VAL)
def test_LinkedList_insert(a):
    from linked_list import LinkedList
    this_list = LinkedList([1])
    this_list.insert(a)
    assert this_list.head.data == a

# _*_ Coding: utf-8 _*_
import pytest

TEST_LIST = [
    ([]),
    ([1,2,3,4,5]),
    (['bob', 'george', [1,2], (1,2)]),
    ([1]),
]

def test_deque_append():
    from src.deque import Deque
    test_deque = Deque([1,2,3,4,5,])
    test_deque.append('bob')
    assert test_deque.peek() == 'bob'
    #assert test_deque.tail.data == 'bob'

def test_deque_appendleft():
    from src.deque import Deque
    test_deque = Deque([1,2,3,4,5,])
    test_deque.appendleft('bob')
    assert test_deque.peekleft() == 'bob'
    #assert test_deque.head.data == 'bob'

def test_deque_pop_1():
    from src.deque import Deque
    test_deque = Deque([1,2,3,4,5,])
    assert test_deque.pop() == 1

def test_deque_pop_2():  
    from src.deque import Deque
    test_deque = Deque()
    with pytest.raises(AttributeError):
        test_deque.pop() 

def test_deque_popleft_1():
    from src.deque import Deque
    test_deque = Deque([1,2,3,4,5,])
    assert test_deque.popleft() == 5

def test_deque_popleft_2():  
    from src.deque import Deque
    test_deque = Deque()
    with pytest.raises(AttributeError):
        test_deque.popleft() 

def test_deque_peek():
    from src.deque import Deque
    test_deque = Deque([1,2,3,4,5,])
    assert test_deque.peek() == 1

def test_deque_peekleft():
    from src.deque import Deque
    test_deque = Deque([1,2,3,4,5,])
    assert test_deque.peekleft() == 5

@pytest.mark.parametrize('a', TEST_LIST)
def test_deque_size(a):
    from src.deque import Deque
    test_deque = Deque(a)
    assert test_deque.size() == len(a)





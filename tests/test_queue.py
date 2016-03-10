import pytest


def test_q_peek():
    from src.queue import Queue
    test_q = Queue()
    assert test_q.peek() is None


def test_q_peek_2():
    from src.queue import Queue
    test_q = Queue()
    val = 6
    test_q.enqueue(val)
    assert test_q.peek() == val


def test_q_peek_3():
    from src.queue import Queue
    test_q = Queue()
    val = 6
    test_q.enqueue(val)
    test_q.enqueue("bob")
    assert test_q.peek() == 6


def test_q_deq():
    from src.queue import Queue
    test_q = Queue()
    val = 6
    test_q.enqueue(val)
    test_q.enqueue("bob")
    assert test_q.dequeue() == 6


def test_q_deq_2():
    from src.queue import Queue
    test_q = Queue()
    val = 6
    test_q.enqueue(val)
    test_q.enqueue("bob")
    peeked = test_q.peek()
    assert test_q.dequeue() == peeked

def test_q_deq_3():
    from src.queue import Queue
    test_q = Queue()
    with pytest.raises(AttributeError):
        test_q.dequeue()

def test_q_size():
    from src.queue import Queue
    test_q = Queue()
    test_q.enqueue(2)
    test_q.enqueue("bob")
    assert test_q.size == 2

def test_q_size_2():
    from src.queue import Queue
    test_q = Queue()
    assert test_q.size == 0

def test_q_size_3():
    from src.queue import Queue
    test_q = Queue()
    test_q.enqueue(2)
    test_q.enqueue("bob")
    test_q.dequeue()
    assert test_q.size == 1


def test_q_empty():
    from src.queue import Queue
    test_q = Queue()
    assert test_q.is_empty


def test_q_empty_2():
    from src.queue import Queue
    test_q = Queue()
    test_q.enqueue(2)
    test_q.dequeue()
    assert test_q.is_empty


def test_q_empty_3():
    from src.queue import Queue
    test_q = Queue()
    test_q.enqueue(2)
    assert not test_q.is_empty

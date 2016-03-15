def test_heap_push():
    from src.heap import Heap
    test_heap = Heap()
    test_heap.push(1)
    assert test_heap.root.data == 1


def test_heap_push2():
    from src.heap import Heap
    test_heap = Heap()
    test_heap.push(1)
    test_heap.push(3)
    assert test_heap.root.data == 3


def test_heap_push3():
    from src.heap import Heap
    test_heap = Heap()
    test_heap.push(7)
    test_heap.push(3)
    assert test_heap.root.data == 7


# def test_heap_push4():
#     test_heap = Heap()
#     test_heap.push(7)
#     test_heap.push(3)
#     assert len(test_heap.index) == 2

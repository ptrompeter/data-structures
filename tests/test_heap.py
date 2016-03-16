def test_heap_push():
    from src.heap import Heap
    test_heap = Heap()
    test_heap.push(1)
    assert test_heap.root == 1


def test_heap_push2():
    from src.heap import Heap
    test_heap = Heap()
    test_heap.push(1)
    test_heap.push(3)
    assert test_heap.root == 3


def test_heap_push3():
    from src.heap import Heap
    test_heap = Heap()
    test_heap.push(7)
    test_heap.push(3)
    assert test_heap.root == 7

def test_heap_pop_simple():
    from src.heap import Heap
    test_heap = Heap([2,4,6])
    test_value = test_heap.root
    assert test_heap.pop() == test_value 

def test_heap_pop_root_is_maxval():
    from src.heap import Heap
    test_heap = Heap([2,4,6])
    test_value = test_heap.pop()
    assert test_value >= max(test_heap.heapList[1:])

def test_heap_pop_removed():
    from src.heap import Heap
    test_heap = Heap([2,4,6])
    test_value = test_heap.pop()
    assert test_value not in test_heap.heapList

def test_heap_pop_didnt_kill_list():
    from src.heap import Heap
    test_heap = Heap([2,4,6])
    test_value = test_heap.pop()
    assert len(test_heap.heapList) == 3

def test_heap_pop_big_list():
    from src.heap import Heap
    big_list = [1,9,6,2,3,7,4,5,9,1,2,5,4,6,8,7,2,3,4,9,8,7,6,1,3,4,6,7,9,0,1]
    test_heap = Heap(big_list)
    test_value = test_heap.pop()
    assert test_value == max(big_list)

# def test_heap_root_is_true():
#     from src.heap import Heap
#     test_heap = Heap([2,4,6])
#     assert test_heap.root

# def test_heap_root_is_expected_value():
#     from src.heap import Heap
#     test_heap = Heap([2,4,6])
#     assert test_heap.root == 6


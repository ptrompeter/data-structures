import pytest

VAL_LIST = [
    ([3, 7, 5], 1, ),
    ([1], 'peas'),
    (['cat', 'dog', 'fish', 'turtle'], True),
]


@pytest.mark.parametrize('a, b', VAL_LIST)
def test_pop(a, b):
    from src.stacks import Stack
    test_stack = Stack(a)
    test_stack.push(b)
    assert test_stack.pop() == b


@pytest.mark.parametrize('a', VAL_LIST)
def test_pop_1(a):
    from src.stacks import Stack
    test_stack = Stack(a)
    assert test_stack.pop() == a[-1]


def test_pop_2():
    from src.stacks import Stack
    test_stack = Stack()
    with pytest.raises(AttributeError):
        test_stack.pop()

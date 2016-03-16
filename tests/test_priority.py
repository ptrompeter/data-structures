from src.priority import Priority

TEST_LIST = [
    (2, 1),
    (5, 1),
    (1, 1),
    (2, 2),
    (1, 2),
    (2, 3),
    (5, 2),
    (4, 1),
    (6, 1),
    (8, 1),
    (1, 3),
    (2, 4),
]

def test_pri_push():
    test_pri = Priority()
    test_pri.push((1, 'a'))
    assert test_pri.plist[0] == (1, 'a')


def test_pri_push1():
    test_pri = Priority()
    test_pri.push((3, 'a'))
    test_pri.push((3, 'b'))
    test_pri.push((3, 'c'))
    test_pri.push((3, 'd'))
    assert test_pri.plist[0][1] == 'a'


def test_pri_push2():
    test_pri = Priority()
    test_pri.push((3, 'a'))
    test_pri.push((3, 'b'))
    test_pri.push((3, 'c'))
    test_pri.push((3, 'd'))
    test_pri.push((2, 'a'))
    assert test_pri.plist[0] == (2, 'a')

def test_pri_push3():
    test_pri = Priority(TEST_LIST)
    assert test_pri.plist[0][0] == 1

def test_pri_push4():
    test_pri = Priority(TEST_LIST)
    assert test_pri.plist[0] == (1, 1)


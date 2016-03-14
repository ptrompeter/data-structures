# _*_ Coding: utf-8 _*_
from double_linked_list import DblList


class Deque(object):
    """Create a Deque class."""
    def __init__(self, value=[]):
        """Initialize a new instance of Deque based upon a conposition of DblList"""
        self.dll = DblList(value)

    def append(self, value):
        self.dll.append(value)

    def appendleft(self, value):
        self.dll.insert(value)

    def pop(self):
        return self.dll.shift()

    def popleft(self):
        return self.dll.pop()

    def peek(self):
        return self.dll.tail.data

    def peekleft(self):
        return self.dll.head.data

    def size(self):
        cursor = self.dll.head
        if cursor is None:
            return 0
        if cursor == self.dll.tail:
            return 1

        counter = 1
        while cursor != self.dll.tail:
            counter += 1
            cursor = cursor.next_node
        return counter
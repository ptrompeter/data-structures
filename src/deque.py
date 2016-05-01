# _*_ Coding: utf-8 _*_
from double_linked_list import DblList


class Deque(object):
    """Create a Deque class."""
    def __init__(self, value=[]):
        """Initialize a new instance of Deque based upon a conposition of DblList"""
        self.dll = DblList(value)

    def append(self, value):
        """Append a value to the deque."""
        self.dll.append(value)

    def appendleft(self, value):
        """Append a value to the front of the deque."""
        self.dll.insert(value)

    def pop(self):
        """Pop a value from the deque"""
        return self.dll.shift()

    def popleft(self):
        """Pop a value from the front of the deque."""
        return self.dll.pop()

    def peek(self):
        """Return the tail of the deque."""
        return self.dll.tail.data

    def peekleft(self):
        """Return the head of the deque."""
        return self.dll.head.data

    def size(self):
        """Return the number of objects in the deque."""
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

# _*_ coding: utf-8 _*_
from linked_list import LinkedList


class Stack(object):
    """Create Stack Class."""

    def __init__(self, value=[]):
        """Initialize new instance of Stack."""
        self.linked = LinkedList(value)

    def pop(self):
        """Pop first item off of Stack."""
        return self.linked.pop()

    def push(self, val):
        """Push value to front of Stack."""
        self.linked.insert(val)

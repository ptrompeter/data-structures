# _*_ coding: utf-8 _*_
from linked_list import Node
from linked_list import LinkedList


class Stack(object):
    """Create Stack Class."""

    def __init__(self, value=[]):
        """Initialize new instance of Stack."""
        self.linked = LinkedList(value)

    def pop(self):
        """Pop first item off of Stack."""
        popped = self.linked.pop()
        return popped

    def push(self, val):
        """Push value to front of Stack."""
        self.linked.insert(val)

    def display(self):
        """Display Stack Instance"""
        self.linked.display()


# _*_ coding: utf-8 _*_
from linked_list import LinkedList
from linked_list import Node

class Queue(LinkedList):
    """Queue is subclass of linkedlist. Uses LinkedList.pop in dequeue."""

    def __init__(self):
        self.head = None
        self.size = 0
        self.is_empty = True

    def enqueue(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.is_empty = False
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = node
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
        if self.size == 0:
            self.is_empty = True
        return self.pop()


    def peek(self):
        try:
            return self.head.data
        except AttributeError:
            return None

#insert append pop shift remove

from linked_list import LinkedList
from linked_list import Node

class Dbl_node(object):
    """Make subclass of Node class"""
    def __init__(self, data=None, next_node=None,  previous_node=None):
        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_prev(self):
        return self.previous_node

    def set_prev(self, new_prev):
        self.previous_node = new_prev


class Dbl_list(LinkedList):
    """Create a subclass of LinkedList"""
    def __init__(self, values=[]):
        """Initialize a new subclass"""
        self.values = values
        self.head = Dbl_node(values[0])
        self.tail = self.head
        for i in range(1, len(values)):
                self.insert(values[i])


    def insert(self, val):
        inserted_node = Dbl_node(val, self.head)
        self.head.previous_node = inserted_node
        self.head = inserted_node


    def append(self, val):
        inserted_node = Dbl_node(val, previous_node = self.tail)
        self.tail.next_node = inserted_node
        self.tail = inserted_node        


    def pop(self):
        val = super(Dbl_list, self).pop()
        self.head.previous_node = None
        return val


    def shift(self):
        shifted = self.tail.data
        self.tail = self.tail.previous_node
        return shifted

    def remove(self, node):
        current = self.head
        target_node = node
        if target_node == current:
            self.pop()
        elif target_node == self.tail:
            self.shift()
        else:
            while current.next_node:
                try:
                    if current.next_node == target_node:
                        current.next_node = target_node.next_node
                        target_node = current.next_node
                        next = current.next_node
                        next.previous_node = current.previous_node
                        break
                    current = current.next_node
                except AttributeError:
                    pass
            else:
                raise AttributeError



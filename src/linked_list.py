# _*_ coding: utf-8 _*_


class Node(object):
    """Make Class Node."""

    def __init__(self, data=None, next_node=None):
        """Init Node Instance."""
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    """Make Class LinkedList."""

    def __init__(self, values=[]):
        """Initialize New instance of LinkedList."""
        self.values = values
        self.head = None
        for i in values:
            self.insert(i)

    def insert(self, val):
        """Insert value 'val' at the head of the list."""
        inserted_node = Node(val, self.head)
        self.head = inserted_node

    def pop(self):
        """Pop first value off the head of the list and return it."""
        popped = self.head
        try:
            self.head = popped.next_node
        except AttributeError:
            self.head = None
        return popped.data

    def size(self):
        """Return length of list."""
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next_node
        return counter

    def search(self, val):
        """Will return the node containing 'val in the list if present. Else None."""
        node = self.head
        while node:
            try:
                if node.data == val:
                    return node
                node = node.next_node
            except AttributeError:
                return None
        else:
            return None

    def remove(self, node):
        """Remove given node from the list. Node must be item in list."""
        if node == self.head:
            self.head = node.next_node
            return
        current = self.head
        while current.next_node:
            try:
                if current.next_node == node:
                    current.next_node = node.next_node
                    break
                current = current.next_node
            except AttributeError:
                break

    def display(self):
        """Print List as Python Tuple Literal."""
        display_list = []
        current = self.head
        while current:
            data = "'{}'".format(current.data) if isinstance(current.data, str) else current.data
            display_list.append("{},".format(data))
            current = current.next_node
        return "({})".format(" ".join(display_list))

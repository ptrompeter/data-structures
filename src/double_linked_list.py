from linked_list import LinkedList


class DblNode(object):
    """Make  Node Object with data, next, and previous node."""

    def __init__(self, data=None, next_node=None, previous_node=None):
        """Init Node with optional args Data, Next_node, Previous_node."""
        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node


class DblList(LinkedList):
    """Create a subclass of LinkedList."""
    def __init__(self, values=[]):
        """Initialize New instance of LinkedList."""
        self.values = values
        self.head = None
        for i in values:
            self.insert(i)


    # using LinkedList __init__ for DblList
    def insert(self, val):
        """Insert Node at the front (head) of list."""
        inserted_node = DblNode(val, self.head)
        if not self.head:
            self.head = inserted_node
            self.tail = self.head
        self.head.previous_node = inserted_node
        self.head = inserted_node

    def append(self, val):
        """Append New node to back (tail) of list."""
        inserted_node = DblNode(val, previous_node=self.tail)
        self.tail.next_node = inserted_node
        self.tail = inserted_node

    def pop(self):
        """Remove Node from Front (head) of list."""
        val = super(DblList, self).pop()
        self.head.previous_node = None
        return val

    def shift(self):
        """Remove Node from Back (Tail) of list."""
        shifted = self.tail.data
        self.tail = self.tail.previous_node
        return shifted

    def remove(self, node):
        """Find and remove node from anywhere in list."""
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

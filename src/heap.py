# -*- coding: utf-8 -*-a


class Node(object):
    """Return."""

    def __init__(self, data, index, left=None, right=None, parent=None):
        """Return."""
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data
        self.index = index


class Heap(object):
    """Return."""

    def __init__(self, values=[]):
        """Return."""
        self.root = None
        # self.size = 0
        self.nodes = []
        for i in values:
            self.push()

    def pop(self):
        """Return."""
        pass

    def push(self, data):
        """Return."""
        new_node = Node(data, len(self.nodes) +1)
        self.nodes.append(new_node)
        if self.root is None:
            self.root = new_node
        else:
            new_node.parent = self.nodes[(new_node.index // 2) -1]
            while new_node.data > new_node.parent.data:
                parentNode = new_node.parent
                parentIndex = new_node.parent.index
                childNode = new_node
                childIndex = new_node.index

                new_node.index = parentIndex
                new_node.parent.index = childIndex

                self.nodes[childIndex - 1] = parentNode
                self.nodes[parentIndex - 1] = childNode
                if new_node.index == 1:
                    self.root = new_node
                    break
                else:
                    new_node.parent = self.nodes[(new_node.index // 2) -1]

# -*- coding: utf-8 -*-a


class Heap(object):
    """Return."""

    def __init__(self, values=[]):
        """Return."""
        self.root = None
        self.size = 0
        self.heapList = [None]
        for i in values:
            self.push()

    def swap_down(self, root):

    def pop(self):
        """Return."""
        self.root = self.heapList[self.size]
       if self.root < self.heapList[]

    def swap_up(self, i):
        """Take index of starting node. If starting node > parent, swap places, set new parent."""
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i //2]
            else:
                break
            i = i // 2


    def push(self, data):
        """Make new node. Increment size. Append node to heapList list. Check for swap up conditions."""
        self.size += 1
        self.heapList.append(data)
        if self.heapList[self.size] > self.heapList[self.size // 2]:
            self.swap_up(self.size)
        self.root = self.heapList[1]

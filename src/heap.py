# -*- coding: utf-8 -*-a


class Heap(object):
    """Return."""

    def __init__(self, values=[]):
        """Return."""
        self.root = None
        self.size = 0
        self.heapList = [None]
        for i in values:
            self.push(i)

    # def swap_down(self, root):
    #     pass

    def pop(self):
        """Return."""
        popped_value = self.heapList[1]
        pos = 1
        startval = self.heapList.pop()
        self.heapList[pos] = startval
        while pos < len(self.heapList) // 2:
            big = self._bigger_child(pos)
            if self.heapList[pos] < self.heapList[big]:
                self.heapList[pos], self.heapList[big] = self.heapList[big], self.heapList[pos]
                pos = big
            else: break
        return popped_value

    def _bigger_child(self, index):
        """Return the index of the larger child."""
        if self.heapList[2 * index] < self.heapList[2 * index + 1]:
            return 2 * index + 1
        else:
            return 2 * index


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
        self.swap_up(self.size)
        self.root = self.heapList[1]

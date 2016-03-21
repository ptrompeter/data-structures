class Priority(object):
    """Return."""

    def __init__(self, values=[]):
        """Return."""
        self.plist = []
        for i in values:
            self.push(i)

    def _swap_up(self, i):
        while (i + 1) // 2 > 0:
            if self.plist[i][0] < self.plist[i // 2][0]:
                self.plist[i], self.plist[i // 2] = self.plist[i // 2], self.plist[i]
            else:
                break
            i = i // 2

    def push(self, tup):
        self.plist.append(tup)
        self._swap_up(len(self.plist) - 1)

    def pop(self):
        popped_value = self.plist[0]
        startval = self.plist.pop()
        pos = 0
        self.plist[pos] = startval
        while pos < len(self.plist) // 2:
            priority = self._higher_priority_child(pos)
            if self.plist[priority] < self.plist[pos]:
                self.plist[pos], self.plist[priority] = self.plist[priority], self.plist[pos]
                pos = priority
            else: break
        return popped_value

    def _higher_priority_child(self, index):
        """Return the index of the larger child."""
        if self.plist[(2 * index) + 1][0] > self.plist[(2 * index + 1) + 1][0]:
            return (2 * index + 1) + 1
        else:
            return (2 * index) + 1

    def peek(self):
        return self.plist[0]

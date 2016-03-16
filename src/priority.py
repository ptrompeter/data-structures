

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
        import pdb; pdb.set_trace()
        self.plist.append(tup)
        self._swap_up(len(self.plist) - 1)

    def pop(self):
        pass

    def peek(self):
        return self.plist[0]

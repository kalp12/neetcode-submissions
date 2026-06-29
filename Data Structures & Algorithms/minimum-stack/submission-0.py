class MinStack:

    def __init__(self):
        self.mn = []
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        val = min(val, self.mn[-1] if self.mn else val)
        self.mn.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.mn.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mn[-1]

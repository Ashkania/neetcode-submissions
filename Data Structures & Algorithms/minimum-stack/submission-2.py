class MinStack:

    def __init__(self):
        self.container = []
        self.minvals = []

    def push(self, val: int) -> None:
        self.container.append(val)
        if not self.minvals:
            self.minvals.append(val)
        else:
            self.minvals.append(min(self.minvals[-1], val))

    def pop(self) -> None:
        self.container.pop()
        self.minvals.pop()

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        # return min(self.container)
        return self.minvals[-1]

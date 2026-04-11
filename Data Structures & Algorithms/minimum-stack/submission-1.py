class MinStack:

    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        if not self.values:
            self.values.append((val, val))
        else:
            current_min = self.values[-1][1]
            self.values.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.values.pop()

    def top(self) -> int:
        return self.values[-1][0]

    def getMin(self) -> int:
        return self.values[-1][1]
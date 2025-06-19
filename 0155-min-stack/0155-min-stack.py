class MinStack:

    def __init__(self):
        self.stackMain = []
        self.stackMin = []

    def push(self, val: int) -> None:
        self.stackMain.append(val)
        if not self.stackMin or self.stackMin[-1] >= val:
            self.stackMin.append(val)

    def pop(self) -> None:
        if self.stackMin[-1] == self.stackMain.pop():
            self.stackMin.pop()

    def top(self) -> int:
        return self.stackMain[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
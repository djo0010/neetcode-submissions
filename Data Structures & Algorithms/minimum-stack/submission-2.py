class MinStack:

    def __init__(self):
        self.mainStack = []
        self.prefixStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if len(self.prefixStack) != 0:
            self.prefixStack.append(min(self.prefixStack[-1], val))
        else:
            self.prefixStack.append(val)

    def pop(self) -> None:
        self.mainStack.pop()
        self.prefixStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.prefixStack[-1]
        

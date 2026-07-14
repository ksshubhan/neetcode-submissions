class MinStack:

    def __init__(self):
        self.__index = []

    def push(self, val: int) -> None:
        self.__index.insert(0, val)

    def pop(self) -> None:
        self.__index.pop(0)

    def top(self) -> int:
        return self.__index[0]

    def getMin(self) -> int:
        return min(self.__index)

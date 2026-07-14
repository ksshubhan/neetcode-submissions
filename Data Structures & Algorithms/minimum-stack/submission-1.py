class MinStack:

    def __init__(self):
        # arguably hardest part

        self.__index = []

    def push(self, val: int) -> None:
        # push to the top of the stack which is index 0 
        self.__index.insert(0, val)

    def pop(self) -> None:
        # remove element at the top of the stack which is index 0 
        self.__index.pop(0)

    def top(self) -> int:
        # return element at the top of the stack which is index 0 
        return self.__index[0]

    def getMin(self) -> int:
        return min(self.__index)

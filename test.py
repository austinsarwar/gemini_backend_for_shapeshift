class Stack:
    def __init__(self) -> None:  
        self.__stack = []

    def push(self, value):
        self.__stack.append(value)
    def pop(self):
         self.__stack.self.pop()
    def peak(self):
        return  self.__stack.self[-1]

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peak())
stack.pop()
print(stack.peak())

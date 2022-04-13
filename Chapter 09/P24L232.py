# time spent: 15 min.

class MyQueue:

    def __init__(self):
        self.s = []
        self.aux = []

    def push(self, x: int) -> None:
        for _ in range(len(self.s)):
            self.aux.append(self.s.pop())
        self.s.append(x)
        for _ in range(len(self.aux)):
            self.s.append(self.aux.pop())

    def pop(self) -> int:
        return self.s.pop()

    def peek(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return not self.s

# Permitted Operations: {append(), pop(), s[-1], len(s), __bool__}
        
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

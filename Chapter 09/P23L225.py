#spent 30 min.

class MyStack:
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
        self.length = 0

    def push(self, x: int) -> None:
        self.q1.appendleft(x)
        self.length += 1

    def pop(self) -> int:
        if self.empty(): return None
        for _ in range(self.length - 1):
            self.q2.appendleft(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1
        self.length -= 1
        return self.q2.pop()

    def top(self) -> int:
        if self.empty(): return None
        for _ in range(self.length - 1):
            self.q2.appendleft(self.q1.pop())
        ret = self.q1[-1]
        self.q2.appendleft(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1
        return ret
		
    def empty(self) -> bool:
        return not self.q1

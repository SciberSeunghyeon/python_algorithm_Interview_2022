class MyCircularDeque:

    def __init__(self, k: int):
        self.Q = [None] * k
        self.k = k
        self.front = self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        
        self.front = (self.front - 1) % self.k
        self.Q[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        
        self.Q[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        
        self.Q[self.front] = None
        self.front = (self.front + 1) % self.k
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        
        self.rear = (self.rear - 1) % self.k
        self.Q[self.rear] = None
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.Q[self.front]

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.Q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.Q[self.front] == None

    def isFull(self) -> bool:
        return self.front == self.rear and self.Q[self.front] != None


# What I've learned: BAN LINKED LIST; Python has list, dic, set, deque, str...
# and of course, I have to stop and find another plan, if one approach seems to not be the way.


""" Failed Linked List Solution.
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
        
class MyCircularQueue:

    def __init__(self, k: int):
        head = curr = Node()
        for _ in range(k-1):
            curr.next = Node()
            curr = curr.next
        curr.next = head
        
        self.front = self.rear = Node(val = 0, next = head)
            

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        self.rear.next.val = value
        self.rear = self.rear.next
        if self.front.val == 0: self.front = self.front.next
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        self.front.val = None
        self.front = self.front.next
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.front.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.rear == self.front and not self.rear.val

    def isFull(self) -> bool:
        return self.rear.next == self.front and self.rear.val
"""
"""
[1, 2, 3, None, None]
front     rear
Queue Empty/Full: two ptrs are same

Important Code Snippet: index update.
idx = (idx + 1)mod N
0 <= mod N <= N-1.

Elegant solution.
"""
class MyCircularQueue:

    def __init__(self, k: int):
        self.Q = [None] * k
        self.k = k
        self.front = self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        self.Q[self.rear] = value
        self.rear = (self.rear + 1) % len(self.Q)
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        self.Q[self.front] = None
        self.front = (self.front + 1) % len(self.Q)
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.Q[self.front]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.Q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.Q[self.front] == None

    def isFull(self) -> bool:
        return self.front == self.rear and self.Q[self.front] != None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

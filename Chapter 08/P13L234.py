# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return True  #전처리의 미학

        deq = collections.deque()
        
        while head:
            deq.append(head.val)
            head = head.next  #놓치지 않는 미학
            
        while len(deq) >=  2:
            if deq.pop() != deq.popleft():
                return False
            
        return True
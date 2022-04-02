# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dq = collections.deque()
        
        while head:
            dq.appendleft(head)
            head = head.next
        
        DUMMY = chain = ListNode() 
        
        for node in dq:
            chain.next = node
            chain = chain.next
        
        chain.next = None
            
        return DUMMY.next

#그래도 공간복잡도 O(n)으로 성공, 새 노드 안 만듬!
#Dummy ->>>> 인풋이 None인 상황에도 깔끔하게 대처 가능, preprocessing보다 빠름
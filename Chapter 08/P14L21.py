# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:     
        DUMMY = chain = ListNode(854) #두 링크드리스트가 모두 None일 경우에 대비!()
  미리 전진시켜놓을 필요가 없음       
        while l1 and l2: #l1 and l2 are runners
            if l1.val <= l2.val:
                chain.next = l1 #l1 not changed yet
                l1 = l1.next
            else:
                chain.next = l2
                l2 = l2.next
     #여기까지가 chain의 next에 다음 노드를 달아주는 파트          chain = chain.next #★★★★★ chain을 전진시켜줘야 함!!!
            
        if l1:
            chain.next = l1
        else:
            chain.next = l2
            
                
        return DUMMY.next
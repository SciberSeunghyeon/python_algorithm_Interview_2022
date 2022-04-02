#2. 계산기 구현(더 우아함, 메모리 아낌)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_len(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        if get_len(l1) < get_len(l2):
            l1, l2 = l2, l1
            
        
        answer_dict = []
        
        while l1:
            answer_dict.append(l1.val)
            l1 = l1.next
            
        digit = 0
        while l2:
            answer_dict[digit] += l2.val
            digit += 1
            l2 = l2.next
        ### List Construction Step
        
        for digit in range(len(answer_dict) - 1):
            if answer_dict[digit] >= 10:
                answer_dict[digit] -= 10
                answer_dict[digit + 1] += 1
                
        if answer_dict[-1] >= 10:
            answer_dict[-1] -= 10
            answer_dict.append(1)
        #prevent idxoutofbounds
        
        ### Roundup Step
        DUMMY = chain = ListNode()
            
        for value in answer_dict:
            chain.next = ListNode(value)
            chain = chain.next
            
        return DUMMY.next
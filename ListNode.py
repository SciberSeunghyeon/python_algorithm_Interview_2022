# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def convert_from_list(self, lis):
        head = curr = ListNode(val=lis[0])
        for idx in range(1, len(lis)):
            curr.next = ListNode(val=lis[idx])
            curr = curr.next
        return head

    def traverse(self):
        head = self
        answer = "["
        while head:
            answer += str(head.val) + ","
            head = head.next
        print(answer[:-1] + "]")
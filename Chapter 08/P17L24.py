from ListNode import ListNode
param_1 = ListNode.convert_from_list(ListNode, [1, 2, 3, 4])


class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        # Preprocessing

        DUMMY = ListNode(next=head)
        prev = DUMMY
        curr = prev.next

        head = head.next
        # Variable initialization

        while curr and curr.next:
            # ------------Wall--------------
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr
            # ------------Bigger Wall---------
            prev = curr
            curr = prev.next

        return head
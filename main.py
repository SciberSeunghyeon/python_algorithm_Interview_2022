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

        while curr and curr.next:  # 변수는 prev,curr,next만 사용하기 #아니 대체왜 curr.next 말고 curr도 체크해야 하는 거야??
            # ------------Wall--------------
            prev.next = curr.next
            curr.next = prev.next.next
            prev.next.next = curr
            # ------------Bigger Wall---------
            prev = curr
            curr = prev.next

        return head

swap = Solution.swapPairs(Solution, param_1)
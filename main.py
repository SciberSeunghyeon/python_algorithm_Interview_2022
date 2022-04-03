from ListNode import ListNode
param_1 = ListNode.convert_from_list(ListNode, [1, 2, 3, 4])

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        # Preprocessing

        n1 = head
        n2 = head.next
        back = n1

        head = n2  # we won't use head until return

        n1.next = n2.next
        n2.next = n1
        # First Time
        while back.next.next:
            back = n1
            n1 = back.next
            n2 = back.next.next
            # ------------Wall--------------
            back.next = n2  # curr points n2
            n1.next = n2.next  # n2 points n1
            n2.next = n1  # n1 points n2's next
            # ------------Bigger Wall---------

        return head

swap = Solution.swapPairs(Solution, param_1)
print(param_1)
#
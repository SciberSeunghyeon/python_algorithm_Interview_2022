from ListNode import ListNode

param_1 = ListNode.convert_from_list(ListNode, [1, 2, 3, 4, 5, 6])

# Started at Mon Apr  4 23:11:43 KST 2022
"""
My Idea : make two heads, 'odd' and 'even' respectively. and just attach two!
"""


class Solution:
    def oddEvenList(self, head):
        if (not head) or (not head.next) or (not head.next.next):
            return head
        # assumes len(head) >= 3.

        odd_head = odd_current = head
        even_head = even_current = head.next
        head = head.next.next

        counter = 3
        while head:
            if counter % 2:  # odd case
                odd_current.next = head
                odd_current = odd_current.next
            else:
                even_current.next = head
                even_current = even_current.next
            head = head.next; counter += 1  # stupidly forgotten point 1.
            # -_-YOU SHOULD MOVE HEAD ptr FORWARD, AFTER PROCESSING NODE!!

        odd_current.next = None; even_current.next = None  # SPF 2
        # -_-IF NOT, INFINITE LOOP EMERGES. [1, 3, 5, 2, 4 but 4 points 5 then infloop
        odd_current.next = even_head

        print(f'Counter = {counter}')

        return odd_head


param_1.traverse()

Solution.oddEvenList(Solution, param_1).traverse()

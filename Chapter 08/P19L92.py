from ListNode import ListNode

param_1 = ListNode.convert_from_list([1,2,3,4,5])

# Started at Tue Apr  5 00:32:34 KST 2022
# Finished at
"""
My Idea : [1,2,3,4,5] and left, right = 2, 4
Then, TARGET = [1,4,3,2,5]
연결리스트의 최대 특징은 정방향 순차적 접근밖에 되지 않는다는 것. 결국 무엇을 처리하든간에 왼쪽에서 오른쪽 방향이어야만함!!
13245(pulls 3 to left position)
14325(pulls 4 to left)
just PULL the right element to left, and continue this!
"""


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not head or left == right:
            return head
        # Preproc. of case len == 0 or 1
        if not head.next.next:
            head.next.next = head
            head = head.next
            head.next.next = None
            return head
        # Preproc. of case len == 2

        # from this, only cases of len <= 3
        left_fisher = real_head_before = ListNode(next = head)
        #DUMMY!! for left fisher, in case of pulling nodes to position 1. it copes with case left == 1
        for i in range(left - 1):
            left_fisher = left_fisher.next
        bef = left_fisher.next
        pull = bef.next
        tmp = pull.next

        for i in range(right - left):
            pull.next = left_fisher.next
            left_fisher.next = pull
            bef.next = tmp

            pull, tmp = tmp, tmp.next if tmp else None # It copes with case (right == last_no).
            #Ternary Operators from Python

        return real_head_before.next

Solution.reverseBetween(Solution, param_1, 4, 5).traverse()
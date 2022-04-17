class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        setattr(ListNode, "__lt__", lambda self, other: self.val < other.val)

        for head in lists:
            while head:
                heapq.heappush(pq, head)
                head = head.next
        new_head = curr = ListNode() # prevents returning None #startpoint handling

        for i in range(len(pq)):
            curr.next = heapq.heappop(pq)
            curr = curr.next

        curr.next = None # prevents cycle #endpoint handling
        return new_head.next

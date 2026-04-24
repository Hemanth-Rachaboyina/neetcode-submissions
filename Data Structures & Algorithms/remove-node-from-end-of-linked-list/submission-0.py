# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        curr = head
        count = 0

        # Step 1: find length
        while curr:
            count += 1
            curr = curr.next

        target = count - n  # node BEFORE the one we delete

        # Special case: remove head
        if target == 0:
            return head.next

        curr = head

        # Step 2: go to node before target
        for _ in range(target - 1):
            curr = curr.next

        # Step 3: delete node
        curr.next = curr.next.next

        return head



        
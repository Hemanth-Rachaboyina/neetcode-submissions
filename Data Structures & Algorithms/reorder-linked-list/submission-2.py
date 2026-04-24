# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # STEP 1: Find the middle of the linked list using slow & fast pointers
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next          # moves 1 step
            fast = fast.next.next    # moves 2 steps

        # Now 'slow' is at the middle node

        # STEP 2: Reverse the second half of the list
        second = slow.next           # start of second half
        prev = slow.next = None      # break the list into two halves

        while second:
            next_node = second.next  # store next node
            second.next = prev       # reverse pointer
            prev = second            # move prev forward

            print(prev)              # (debug) prints current reversed node
            second = next_node       # move to next node

        # Now 'prev' is the head of the reversed second half

        # STEP 3: Merge the two halves alternately
        first, second = head, prev

        while second:
            # store next pointers
            tmp1, tmp2 = first.next, second.next

            # link nodes alternately
            first.next = second
            second.next = tmp1

            # move pointers forward
            first, second = tmp1, tmp2
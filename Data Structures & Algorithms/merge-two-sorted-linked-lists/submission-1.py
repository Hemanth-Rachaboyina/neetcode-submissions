# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy node to act as the start of the merged list
        # 'node' is a pointer that will move along the new list
        dummy = node = ListNode()

        # Traverse both lists while neither is empty
        while list1 and list2:
            # Compare current values of both lists
            if list1.val < list2.val:
                # Attach the smaller node (list1) to the merged list
                node.next = list1
                # Move list1 pointer forward
                list1 = list1.next
            else:
                # Attach the smaller node (list2) to the merged list
                node.next = list2
                # Move list2 pointer forward
                list2 = list2.next
            
            # Move the 'node' pointer forward in the merged list
            node = node.next
        
        # At least one list is now empty
        # Attach the remaining nodes from the non-empty list
        node.next = list1 or list2

        # Return the merged list, skipping the dummy node
        return dummy.next

        
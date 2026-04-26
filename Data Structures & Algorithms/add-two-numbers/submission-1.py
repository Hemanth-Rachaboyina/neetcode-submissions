# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 =l1
        curr2 = l2
        string1 = ""
        string2= ""
        int1 = 0
        int2 = 0

        while curr1:
            string1 = string1 + str(curr1.val)
            curr1 = curr1.next
        while curr2:
            string2 = string2 + str(curr2.val)
            curr2 = curr2.next
        
        int1 = int(string1[::-1])
        int2 = int(string2[::-1])

        int3 = int1+int2

        def build_list(s: str) -> ListNode:
            dummy = ListNode(0)   # temporary head
            current = dummy

            s = s[::-1]

            for ch in s:
                current.next = ListNode(int(ch))  # convert char to int
                current = current.next

            return dummy.next  # actual head

        
        return build_list(str(int3))
    
        

        
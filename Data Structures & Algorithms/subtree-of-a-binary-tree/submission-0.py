# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check_l_r(node1, node2):
            # both empty
            if not node1 and not node2:
                return True
            
            # one empty
            if not node1 or not node2:
                return False
            
            # value mismatch
            if node1.val != node2.val:
                return False
            
            # check left and right recursively
            return (check_l_r(node1.left, node2.left) and
                    check_l_r(node1.right, node2.right))
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if not node:
                continue
            
            # potential match found
            if node.val == subRoot.val:
                if check_l_r(node, subRoot):
                    return True
            
            # keep searching
            stack.append(node.left)
            stack.append(node.right)
        
        return False


            
        
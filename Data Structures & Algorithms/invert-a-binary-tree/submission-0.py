# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# Input: root = [1,2,3,4,5,6,7]   , [1]

# Output: [1,3,2,7,6,5,4]

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return None 
        
        queue = deque([root])
        print("1st attempt",queue)
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right , node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        queue = deque([root])   # Use queue instead of stack
        final = []

        while queue:
            level = []

            for _ in range(len(queue)):
                curr = queue.popleft()   # FIFO → correct order
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            final.append(level)

        return final

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        final = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                curr = queue.popleft()

                # If it's the last node of this level → rightmost
                if i == level_size - 1:
                    final.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return final

        
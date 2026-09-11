# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = [float('-inf')]
        def height(node):
            if not node:
                return 0
            
            lh = max(height(node.left), 0)
            rh = max(height(node.right), 0)

            m[0] = max(m[0], node.val + lh + rh)

            return node.val + max(lh, rh)

        height(root)
        return m[0]

        
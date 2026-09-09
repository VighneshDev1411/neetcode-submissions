class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0
            
            lh = height(node.left)
            rh = height(node.right)

            return 1 + max(lh, rh)

        return height(root)
        
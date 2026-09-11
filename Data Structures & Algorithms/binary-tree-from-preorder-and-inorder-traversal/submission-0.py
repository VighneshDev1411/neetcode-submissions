# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # For O(1) time lookups 
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        preorder_idx = [0]

        if not preorder or not inorder:
            return None 

        def build(left, right):
            if left > right:
                return None 

            root_val = preorder[preorder_idx[0]]

            root = TreeNode(root_val)

            preorder_idx[0] += 1

            mid = inorder_map[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)


        
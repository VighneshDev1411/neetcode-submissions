# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def ks(node):
            count = 0
            stack = []
            curr = node
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                    
                curr = stack.pop()
                count += 1

                if count == k:
                    return curr.val

                curr = curr.right

        ans = ks(root)
        return ans 
        
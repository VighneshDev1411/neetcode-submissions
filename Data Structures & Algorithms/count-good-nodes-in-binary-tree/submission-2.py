class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        path = []
        result = []
        def dfs(node, max_so_far):
            if not node:
                return 0

            # path.append(node.val)
            count = 1 if node.val >= max_so_far else 0
        
            # if not node.left and not node.right:
                # result.append(path[:])

            max_so_far = max(node.val, max_so_far)

            count += dfs(node.left, max_so_far)
            count += dfs(node.right, max_so_far)

            # path.pop()

            return count
        
        return dfs(root, root.val)
        

            


        
        
        
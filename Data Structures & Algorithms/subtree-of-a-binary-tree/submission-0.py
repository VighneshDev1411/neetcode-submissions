class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(s, t):
            if not s and not t:
                return True
            
            if not s or not t:
                return False 
            
            if s.val != t.val:
                return False
        
            left = isSameTree(s.left, t.left)
            right = isSameTree(s.right, t.right)
            
            return left and right


        if not subRoot:
            return False 

        if not root:
            return False 

        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)






    

        

        
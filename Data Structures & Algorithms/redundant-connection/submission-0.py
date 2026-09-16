class DisjointSet:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n + 1)]
    
    def findUParent(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.findUParent(self.parent[node])

        return self.parent[node]
    
    def unionBySize(self, u, v):
        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)

        if ulp_u == ulp_v:
            return False 
        
        if self.size[ulp_v] > self.size[ulp_u]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ds = DisjointSet(n)

        for u, v in edges:
            if not ds.unionBySize(u, v):
                return [u, v]

        return []














        
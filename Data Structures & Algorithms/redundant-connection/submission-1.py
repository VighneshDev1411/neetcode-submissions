from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)

        # try removing edges starting from the LAST one
        for i in range(n - 1, -1, -1):
            remaining = edges[:i] + edges[i+1:]
            if self.isConnected(n, remaining):
                return edges[i]

        return []

    def isConnected(self, n, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(edges[0][0])  # start DFS from any node in the remaining edges

        return len(visited) == n
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)


        component = 0
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                dfs(node)
                component += 1

        return component
        
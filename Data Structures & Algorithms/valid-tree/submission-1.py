class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_list = {i: [] for i in range(n)}

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        components = 0

        def dfs(node, parent):
            visited.add(node)

            for neighbor in adj_list[node]:

                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True

                elif neighbor != parent:
                    return True

            return False

        for node in range(n):

            if node not in visited:
                components += 1

                # Cycle found
                if dfs(node, -1):
                    return False

        # More than 1 component = disconnected
        if components > 1:
            return False

        return True

        
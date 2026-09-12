class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(numCourses)}
        indegree = {i:0 for i in range(numCourses)}
        

        for u, v in prerequisites:
            adj_list[v].append(u)
            indegree[u] += 1

        result = []

        queue = deque()

        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []
        
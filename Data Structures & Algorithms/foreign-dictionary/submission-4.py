class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set(''.join(words))

        K = len(chars)

        adj = {i:set() for i in chars}
        indegree = {i:0 for i in chars}

        order = []

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            foundDiff = False

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    
                    foundDiff = True
                    break

            if not foundDiff and len(w1) > len(w2):
                return ""

        queue = deque()

        for char in chars:
            if indegree[char] == 0:
                queue.append(char)

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in adj[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != K:
            return ""

        return ''.join(order)

        
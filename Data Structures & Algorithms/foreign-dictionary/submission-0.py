class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set(''.join(words))
        K = len(chars)

        adj_list = {char: set() for char in chars}
        indegree = {char: 0 for char in chars}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            found_diff = False

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj_list[w1[j]]:
                        adj_list[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                
                    found_diff = True
                    break
        

            if not found_diff and len(w1) > len(w2):
                return ""
        
        queue = deque()
        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)

        order = []
        while queue:
            char = queue.popleft()
            order.append(char)
            for neighbor in adj_list[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != K:
            return ""
        
        return ''.join(order)




       

        
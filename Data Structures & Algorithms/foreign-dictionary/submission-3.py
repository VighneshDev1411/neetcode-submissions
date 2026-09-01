class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set(''.join(words))

        adj = {c: set() for c in chars}
        inorder = {c: 0 for c in chars}

        k = len(chars)
        print(chars)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            found_diff = False 

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        inorder[w2[j]] += 1
                    
                    found_diff = True
                    break
                
            if not found_diff and len(w1) > len(w2):
                return ""
            
        queue = deque()
        order = []
        for char in inorder:
            if inorder[char] == 0:
                queue.append(char)
            
        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in adj[char]:
                inorder[neighbor] -= 1
                if inorder[neighbor] == 0:
                    queue.append(neighbor)

        
        return ''.join(order) if len(order) == k else ''


                




        
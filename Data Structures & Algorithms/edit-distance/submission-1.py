class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def func(i, j):
            if i < 0:
                return j + 1
            
            if j < 0:
                return i + 1

            if word1[i] == word2[j]:
                return 0 + func(i-1, j - 1)

            if (i, j) in memo:
                return memo[(i, j)]

            x = func(i - 1, j) # Delete
            y = func(i, j - 1) # Insert
            z = func(i - 1, j - 1) # Replace

            memo[(i, j)] = 1 + min(x, y, z)

            return memo[(i, j)]
        
        m, n = len(word1), len(word2)
        return func(m-1, n -1)

        
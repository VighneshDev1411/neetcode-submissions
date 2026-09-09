class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        count = [0]
    
        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count[0] += 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)

        return count[0]
            

        
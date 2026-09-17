class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)

        def isPalindrome(subs):
            return subs == subs[::-1]

        def backtrack(ind, path):
            if ind == n:
                result.append(path[:])
                return 

            for end in range(ind, n):
                substr = s[ind: end + 1]
                if isPalindrome(substr):
                    path.append(substr)
                    backtrack(end + 1, path)
                    path.pop()
                
        backtrack(0, [])
        return result
            

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        have = 0
        need = Counter(t)
        need_count = len(need)
        window = {}
        min_len = float('inf')
        min_start = 0
        left = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1

            while have == need_count:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left 
                
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        if min_len == float('inf'):
            return ""
        
        else:
            return s[min_start:min_start + min_len]






        
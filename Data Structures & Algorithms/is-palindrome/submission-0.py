import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left, right = 0, len(cleaned) - 1
        print(cleaned)
        while left < right :
            if(cleaned[left] != cleaned[right]):
                return False
            left = left + 1
            right = right - 1
        return True

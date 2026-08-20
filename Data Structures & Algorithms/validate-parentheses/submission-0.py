class Solution:
    def isValid(self, st: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for s in st:
            if s in ['(', '{', '[']:
                stack.append(s)

            elif s in mapping:
                if not stack or stack[-1] != mapping[s]:
                    return False
            
                stack.pop()
            

        if len(stack) == 0:
            return True
        else:
            return False
        
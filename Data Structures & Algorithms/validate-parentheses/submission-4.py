class Solution:
    def isValid(self, st: str) -> bool:
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []
        
        for s in st:
            if s in ['(', '{', '[']:
                stack.append(s)
            
            elif s in mapping:
                if not stack or  stack[-1] != mapping[s]:
                    return False 

                stack.pop()

        return True if len(stack) == 0 else False
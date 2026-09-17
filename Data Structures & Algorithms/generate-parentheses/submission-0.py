class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(path, opening, closing):
            if len(path) == 2 * n:
                result.append(''.join(path))
            
            if opening < n:
                path.append('(')
                backtrack(path, opening + 1, closing)
                path.pop()
            
            if closing < opening:
                path.append(')')
                backtrack(path, opening, closing + 1)
                path.pop()

        backtrack([], 0, 0)
        return result


        
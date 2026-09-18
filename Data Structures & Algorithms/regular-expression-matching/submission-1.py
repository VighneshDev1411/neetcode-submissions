class Solution:
    def isMatch(self, s1: str, pat: str) -> bool:
        memo = {}

        def recursion(s, p, i, j):

            # Both string and pattern are completely processed
            if i < 0 and j < 0:
                return True

            # Pattern is finished but string still remains
            if j < 0:
                return False

            # String is finished
            if i < 0:
                # Remaining pattern must be like a*b*c*
                while j >= 0:
                    if p[j] != '*':
                        return False
                    j -= 2

                return True

            # Already calculated
            if (i, j) in memo:
                return memo[(i, j)]

            # Current characters match
            if p[j] == s[i] or p[j] == '.':
                memo[(i, j)] = recursion(s, p, i - 1, j - 1)

            # Current pattern character is '*'
            elif p[j] == '*':
                
                # '*' matches zero occurrences
                zero = recursion(s, p, i, j - 2)

                # '*' matches one or more occurrences
                if p[j - 1] == s[i] or p[j - 1] == '.':
                    one_or_more = recursion(s, p, i - 1, j)
                else:
                    one_or_more = False

                memo[(i, j)] = zero or one_or_more

            # Characters don't match
            else:
                memo[(i, j)] = False

            return memo[(i, j)]

        return recursion(s1, pat, len(s1) - 1, len(pat) - 1)
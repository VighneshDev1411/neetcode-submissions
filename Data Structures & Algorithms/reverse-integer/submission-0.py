class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1

        x = abs(x)
        result = 0

        while x != 0:
            digit = x % 10 
            x = x // 10
            result = result * 10 + digit
        
        result = sign * result 

        return 0 if result < -2**31 or result > 2 ** 31 - 1 else result
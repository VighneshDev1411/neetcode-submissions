class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        if n == 0:
            return 0

        while True:
            n = n & (n - 1)
            count += 1
            if n == 0:
                break

        return count 
        
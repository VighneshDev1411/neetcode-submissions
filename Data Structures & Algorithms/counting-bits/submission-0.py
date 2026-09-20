class Solution:
    def countBits(self, n: int) -> List[int]:
        def count1Bits(n):
            count = 0
            while n:
                n = n & (n - 1)
                count += 1

            return count 

        output = []
        
        i = 0
        while n >= 0:
            bits = count1Bits(i)
            output.append(bits)
            i += 1
            n -= 1

        return output










        
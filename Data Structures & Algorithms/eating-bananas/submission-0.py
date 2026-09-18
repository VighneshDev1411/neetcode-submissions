class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = float('inf')
   

        def isFeasible(bananas):
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i] / mid)

            return total <= h


        while low <= high:
            mid = (low + high) // 2

            if isFeasible(mid):
                ans = min(mid, ans)
                high = mid - 1

            else:
                low = mid + 1
            

        return ans

        
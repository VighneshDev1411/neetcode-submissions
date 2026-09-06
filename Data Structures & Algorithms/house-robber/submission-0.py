class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2 = 0
        prev1 = 0

        for num in nums:
            current = max(prev1, num + prev2)
            prev2 = prev1
            prev1 = current 

        return prev1

            
        


        
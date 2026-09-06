class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev2 = 0
        prev1 = 0
        current1, current2 = 0, 0
        n = len(nums)
        if n == 1:
            return nums[0]
        for num in nums[1:]:
            current1 = max(prev1, num + prev2)
            prev2 = prev1
            prev1 = current1

        ans1 = prev1

        prev1 = 0
        prev2 = 0

        for num in nums[:-1]:
            current2 = max(prev1, num + prev2)
            prev2 = prev1
            prev1 = current2

        ans2 = prev1

        return max(ans1, ans2)


        







        
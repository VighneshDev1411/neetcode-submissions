class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        summ = 0
        for num in nums:
            summ += num
            max_sum = max(max_sum, summ)
            if summ < 0:
                summ = 0

        return max_sum
        
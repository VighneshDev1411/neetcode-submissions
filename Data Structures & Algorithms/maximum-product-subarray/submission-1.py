class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_so_far = max_so_far = result = nums[0]
        for i in range(1, n):
            num = nums[i]

            if num < 0:
                min_so_far, max_so_far = max_so_far, min_so_far
            
            max_so_far = max(num, max_so_far * num)
            min_so_far = min(num, min_so_far * num)

            result = max(result, max_so_far)

        return result






        
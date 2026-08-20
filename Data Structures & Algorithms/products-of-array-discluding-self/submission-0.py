import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [nums[0]]
        l = len(nums)
        res = []
        for i in range(l):
            prefix = nums[0:i]
            suffix = nums[i+1: l]
            new_arr = prefix + suffix
            res.append(math.prod(new_arr))
            new_arr = []
        return res

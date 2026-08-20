from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print(enumerate(nums))
        seen = {}
        for i , num in enumerate(nums):
            complement = target - num
            if(complement in seen):
                return [seen[complement], i]
            seen[num] = i
        return []

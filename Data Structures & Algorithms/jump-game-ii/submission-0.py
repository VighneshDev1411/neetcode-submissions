class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        curr_end = 0
        farthest = 0
        steps = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if curr_end == i:
                steps += 1
                curr_end = farthest

        return steps

        
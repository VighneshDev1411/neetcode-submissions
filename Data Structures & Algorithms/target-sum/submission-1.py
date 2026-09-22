class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = [0]
        memo = {}
        def recursion(ind, target):
            if ind == n:
                if target == 0:
                    return 1
                return 0
            
            if (ind, target) in memo:
                return memo[(ind, target)]
            
            pick = recursion(ind + 1, target - nums[ind])
            not_pick = recursion(ind + 1, target + nums[ind])
            
            memo[(ind, target)] = pick + not_pick

            return memo[(ind, target)]




        return recursion(0, target)
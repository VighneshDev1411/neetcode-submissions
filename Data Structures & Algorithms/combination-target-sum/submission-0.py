class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(ind, path, n, summ):
            if summ == 0:
                result.append(path[:])
                return 
            
            if ind == n or summ < 0:
                return 

            path.append(nums[ind])

            backtrack(ind, path, n, summ - nums[ind])
            path.pop()
            backtrack(ind + 1, path, n, summ)

        result = []
        backtrack(0, [], len(nums), target)
        return result
        
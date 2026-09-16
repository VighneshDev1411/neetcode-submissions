class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(ind, path, n):
            if ind == n:
                result.append(path[:])
                return

            path.append(nums[ind])

            backtrack(ind + 1, path, n)
            path.pop()
            backtrack(ind + 1, path, n)

        result = []
        backtrack(0, [], len(nums))
        return result

        
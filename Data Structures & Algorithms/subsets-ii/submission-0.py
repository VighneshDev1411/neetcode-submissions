class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(ind, path, n):
            if ind == n:
                result.append(path[:])
                return

            path.append(nums[ind])

            backtrack(ind + 1, path, n)
            path.pop()
            next_ind = ind + 1

            while next_ind < n and nums[next_ind] == nums[ind]:
                next_ind += 1

            backtrack(next_ind, path, n)

        result = []
        backtrack(0, [], len(nums))
        return result

        
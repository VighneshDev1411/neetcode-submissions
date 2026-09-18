class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        mini = float('inf')

        while left <= right:
            mid = (left + right) // 2

            mini = min(mini, nums[mid])

            if nums[mid] > nums[right]:
                # mini = min(mini, nums[mid])
                left = mid + 1

            else:
                right = mid - 1

        return mini





        
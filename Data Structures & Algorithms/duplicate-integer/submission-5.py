from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # n = len(nums)
        # nums.sort()
        # for i in range(n - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True

        # return False

        # my_dict = Counter(nums)

        # for key, value in my_dict.items():
        #     if value > 1:
        #         return True

        # return False
        my_set = set()

        for num in nums:
            if num in my_set:
                return True

            my_set.add(num)

        return False





        
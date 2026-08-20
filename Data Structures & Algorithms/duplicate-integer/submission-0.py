from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = Counter(nums)
        # print(my_dict)

        for value in my_dict.values():
            if value > 1:
                return True
                
        return False
       

         
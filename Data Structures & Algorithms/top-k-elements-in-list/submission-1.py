from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = Counter(nums)

        sorted_my_dict = dict(
            sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        )

        
        result = []
      

        for key, value in sorted_my_dict.items():
                result.append(key)
                k -= 1
                if k == 0:
                    break


        return result







        
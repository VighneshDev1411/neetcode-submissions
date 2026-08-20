from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        num_count = Counter(nums)
        print(num_count)

      
        for key, value in sorted(num_count.items(), key=lambda x: x[1],         reverse=True)[:k]:
            if(value >= 1):
                result.append(key)

        return result

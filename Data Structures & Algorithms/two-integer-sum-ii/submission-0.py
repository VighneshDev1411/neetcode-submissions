class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        summ = 0
        while left < right:
            summ = numbers[left] + numbers[right]

            if(summ == target):
                return [left+1, right+1]
            elif(summ > target):
                right = right - 1
            else:
                left = left+1


        
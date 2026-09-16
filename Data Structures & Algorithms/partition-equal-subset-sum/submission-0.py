class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        n = len(arr)
        total = sum(arr)
        target = total // 2

        if total % 2 != 0:
            return False 

        memo = {}

        def backtrack(ind, summ):

            if summ == 0:
                return True

            if ind == n:
                return False

            if (ind, summ) in memo:
                return memo[(ind, summ)] 
            
            pick = backtrack(ind + 1, summ - arr[ind])            
            not_pick = backtrack(ind + 1, summ)

            memo[(ind, summ)] = pick or not_pick

            return memo[(ind, summ)] 

        return backtrack(0, target)

        
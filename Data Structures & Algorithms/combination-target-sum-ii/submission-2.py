class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()

        def backtrack(ind, path, summ):
            if summ == 0:
                result.append(path[:])
                return
            
            if ind == n or summ < 0:
                return 
            
            path.append(candidates[ind])
            backtrack(ind + 1, path, summ - candidates[ind])
            path.pop()

            nxt_ind = ind + 1

            while nxt_ind < n and candidates[nxt_ind] == candidates[ind]:
                nxt_ind += 1

            backtrack(nxt_ind, path, summ)

        result = []
        backtrack(0, [], target)
        return result
        
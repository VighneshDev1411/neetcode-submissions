class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        def nge(nums):
            n = len(nums)
            ans = [-1] * n
            stack = []
            for i in range(n - 1, -1, -1):
                while stack and nums[stack[-1]] <= nums[i]:
                    stack.pop()
                
                if stack:
                    ans[i] = stack[-1]
                

                stack.append(i)

            return ans
        
        output = []
        next_greater_element = nge(temps)
   
        for i, temp in enumerate(temps):
            if next_greater_element[i] - i < 0:
                output.append(0)
            else:
                output.append(next_greater_element[i] - i)

        return output




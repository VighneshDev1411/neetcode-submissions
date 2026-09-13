from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Interview takeaway: Whenever you see "maximum/minimum of every sliding window", think Monotonic Deque.
        """
        dq = deque()
        result = []

        for i in range(len(nums)):
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

            




        
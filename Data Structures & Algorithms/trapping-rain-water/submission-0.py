class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = 0, 0
        n = len(height)
        water = 0
        left, right = 0, n - 1

        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                water += (leftMax - height[left])
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                water += (rightMax-  height[right])
                right -= 1

        return water















        
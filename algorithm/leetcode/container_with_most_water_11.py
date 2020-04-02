from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            high = min(height[l], height[r])
            width = r - l
            ans = max(ans, high * width)

            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return ans

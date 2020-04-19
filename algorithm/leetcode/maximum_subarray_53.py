from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        ans = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            sum = max(nums[i], sum + nums[i])
            ans = max(ans, sum)
        return ans

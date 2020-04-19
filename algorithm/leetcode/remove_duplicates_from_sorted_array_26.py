from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1

        while r < len(nums):
            if nums[l] != nums[r]:
                if r - l > 1: # [1 2 3] 这种不需要原地赋值了
                    nums[l + 1] = nums[r]
                l = l + 1
            r = r + 1

        return l + 1

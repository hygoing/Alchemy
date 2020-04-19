from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1] * 2
        ans[0] = self.binarySearch(nums, target, True)
        ans[1] = self.binarySearch(nums, target, False)
        return ans

    def binarySearch(self, nums: List[int], target, first: bool) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) >> 2)
            if nums[m] == target:
                if first and (m == 0 or nums[m - 1] != target):
                    return m
                elif first:
                    r = m - 1
                elif not first and (m == len(nums) - 1 or nums[m + 1] != target):
                    return m
                elif not first:
                    l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1

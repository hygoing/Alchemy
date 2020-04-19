from time import sleep
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) >> 2)
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[m] > target and nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target and nums[r] >= target:
                    l = m + 1
                else:
                    r = m - 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(solution.search(nums, 0))

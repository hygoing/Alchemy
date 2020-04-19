from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                if m == len(nums) - 1 or nums[m + 1] > target:
                    return m + 1
                else:
                    l = m + 1
            else:
                r = m - 1
        return 0


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 5, 6]
    print(solution.searchInsert(nums, 7))

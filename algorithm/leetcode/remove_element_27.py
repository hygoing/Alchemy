from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
        return i


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    solution = Solution()
    length = solution.removeElement(nums, 2)
    for i in range(0, length):
        print(nums[i])

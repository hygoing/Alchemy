from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        tmp = [0] * len(nums)
        self.recursion(nums, 0, len(nums) - 1, tmp)
        return nums

    def recursion(self, nums: List[int], left, right, tmp: List[int]):
        if left >= right:
            return
        mid = (left + right) // 2
        self.recursion(nums, left, mid, tmp)
        self.recursion(nums, mid + 1, right, tmp)
        self.merge(nums, left, mid, right, tmp)

    def merge(self, nums: List[int], left: int, mid: int, right: int, tmp: List[int]):
        l = left
        r = mid + 1
        i = left

        while l <= mid and r <= right:
            if nums[l] < nums[r]:
                tmp[i] = nums[l]
                l += 1
            else:
                tmp[i] = nums[r]
                r += 1
            i += 1

        while l <= mid:
            tmp[i] = nums[l]
            l += 1
            i += 1

        while r <= right:
            tmp[i] = nums[r]
            r += 1
            i += 1

        for j in range(left, i):
            nums[j] = tmp[j]

if __name__ == "__main__":
    solution = Solution()
    nums = [6, 1, 9, 0, 3, 54, 123, 75, 12, 53]
    solution.sortArray(nums)
    print(nums)

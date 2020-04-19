from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] != 0:
                continue
            if nums[i] == 0 and i == 0:
                return False
            flag = False
            for j in range(i - 1, -1, -1):
                if nums[j] >= i - j + 1:
                    flag = True
                    break
            if not flag:
                return False
        return True

    def canJump(self, nums: List[int]) -> bool:
        r = 0
        for i in range(0, len(nums)):
            if i > r:
                return False
            r = max(r, i + nums[i])
        return True

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.dfs(0, nums, [], ans)
        return ans

    def dfs(self, begin, nums: List[int], tmp: List[int], ans: List[List[int]]):
        ans.append(tmp.copy())
        for i in range(begin, len(nums)):
            if i > begin and nums[i] == nums[i - 1]:
                continue
            tmp.append(nums[i])
            self.dfs(i + 1, nums, tmp, ans)
            tmp.pop()

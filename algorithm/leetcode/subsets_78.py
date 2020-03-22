'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_res = []
        res.append(sub_res)
        self.dfs(0, nums, sub_res, res)
        return res

    def dfs(self, begin: int, nums: List[int], sub_res: List[int], res: List[List[int]]):
        for i in range(begin, len(nums)):
            sub_res.append(nums[i])
            res.append(sub_res.copy())
            self.dfs(i + 1, nums, sub_res, res)
            sub_res.pop()


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.subsets(nums)
    print(res)

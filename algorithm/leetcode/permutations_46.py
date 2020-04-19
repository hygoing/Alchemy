from typing import List, Dict

from algorithm.sort.heap_sort import swap


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # self.dfs(nums, 0, [False] * len(nums), [], ans)
        self.dfs(nums, 0, ans)
        return ans

    def dfs(self, nums: List[int], begin: int, visited: List[bool], sub_ans: List[int], ans: List[List[int]]):
        if begin == len(nums):
            ans.append(sub_ans.copy())

        for i in range(0, len(nums)):
            if not visited[i]:
                visited[i] = True
                sub_ans.append(nums[i])
                self.dfs(nums, begin + 1, visited, sub_ans, ans)
                sub_ans.pop()
                visited[i] = False

    def dfs(self, nums: List[int], begin: int, ans: List[List[int]]):
        if begin == len(nums):
            ans.append(nums.copy())

        for i in range(begin, len(nums)):
            swap(nums, begin, i)
            self.dfs(nums, begin + 1, ans)
            swap(nums, begin, i)


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))

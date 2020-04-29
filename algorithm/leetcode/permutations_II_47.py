from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(0, nums, [False] * len(nums), [], ans)
        return ans

    def dfs(self, begin: int, nums: List[int], visited: List[int], sub: List[int], ans: List[List[int]]):
        if begin == len(nums):
            ans.append(sub.copy())
            return

        i = 0
        while i < len(nums):
            if not visited[i]:
                visited[i] = True
                sub.append(nums[i])
                self.dfs(begin + 1, nums, visited, sub, ans)
                sub.pop()
                visited[i] = False
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i = i + 1
            i = i + 1


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2]
    nums.sort()
    print(solution.permuteUnique(nums))

    a = [87,81,72,62,82,]
    b = [5,4,1.5,4,1]
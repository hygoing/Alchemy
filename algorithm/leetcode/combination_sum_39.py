from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.dfs(candidates, 0, target, [], ans)
        return ans

    def dfs(self, candidates: List[int], begin: int, target: int, tmp: List[int], ans: List[List[int]]):
        if target == 0:
            ans.append(tmp.copy())
            return

        for i in range(begin, len(candidates)):
            if candidates[i] > target:
                continue
            tmp.append(candidates[i])
            self.dfs(candidates, i, target - candidates[i], tmp, ans)
            tmp.pop()


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3, 6, 7]
    print(solution.combinationSum(nums, 7))

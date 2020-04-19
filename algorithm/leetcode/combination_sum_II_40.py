from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        print(candidates)
        self.dfs(candidates, 0, target, [], ans)
        return ans

    def dfs(self, candidates: List[int], begin: int, target: int, tmp: List[int], ans: List[List[int]]):
        if target == 0:
            ans.append(tmp.copy())
            return

        for i in range(begin, len(candidates)):
            if i > begin and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            tmp.append(candidates[i])
            self.dfs(candidates, i + 1, target - candidates[i], tmp, ans)
            tmp.pop()


if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum2([2, 5, 2, 1, 2], 5))

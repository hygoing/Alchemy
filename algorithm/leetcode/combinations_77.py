from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs(1, n, k, [], ans)
        return ans

    def dfs(self, begin: int, n: int, k: int, tmp: List[int], ans: List[List[int]]):
        if len(tmp) == k:
            ans.append(tmp.copy())
            return

        for i in range(begin, n + 1):
            if len(tmp) > k:
                return
            tmp.append(i)
            self.dfs(i + 1, n, k, tmp, ans)
            tmp.pop()

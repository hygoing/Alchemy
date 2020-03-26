'''
sum = 4 * n + 2 - 2 * min(up, n) - 2 * min(left, n)

'''
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                ans += 6 * grid[i][j]
                if grid[i][j] > 0:
                    ans -= 2 * (grid[i][j] - 1)
                if i > 0:
                    ans -= 2 * min(grid[i - 1][j], grid[i][j])
                if j > 0:
                    ans -= 2 * min(grid[i][j - 1], grid[i][j])
        return ans


if __name__ == "__main__":
    solution = Solution()
    l_param = [[1, 0], [0, 2]]
    print(solution.surfaceArea(l_param))

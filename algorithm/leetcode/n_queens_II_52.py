import math
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        visited = [-1] * n
        return self.dfs(0, visited, ans, n)

    def dfs(self, row: int, visited: List[int], count: int, n: int) -> int:
        if row == n:
            print(visited)
            count += 1
            return count

        for column in range(0, n):
            if not self.isValid(row, column, visited):
                continue
            visited[row] = column
            count = self.dfs(row + 1, visited, count, n)
            visited[row] = -1
        return count

    def isValid(self, row: int, column: int, visited: List[int]) -> bool:
        for r in range(0, row):
            if visited[r] == column or math.fabs(row - r) == math.fabs(column - visited[r]):
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.totalNQueens(5))

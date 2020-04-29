import math
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for i in range(0, n)] for j in range(0, n)]

        up, down, left, right = 0, n - 1, 0, n - 1
        i = 1
        while i <= n * n:
            for column in range(left, right + 1):
                ans[up][column] = i
                i = i + 1
            up = up + 1

            for row in range(up, down + 1):
                ans[row][right] = i
                i = i + 1
            right = right - 1

            for column in range(right, left - 1, -1):
                ans[down][column] = i
                i = i + 1
            down = down - 1

            for row in range(down, up - 1, -1):
                ans[row][left] = i
                i = i + 1
            left = left + 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateMatrix(3))

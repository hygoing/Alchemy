from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        level = 0

        while l < r:
            for k in range(l, r):
                i, j = level, k
                curr = matrix[i][j]
                for p in range(0, 4):
                    target = matrix[j][len(matrix) - i - 1]
                    matrix[j][len(matrix) - i - 1] = curr

                    curr = target
                    i, j = j, len(matrix) - i - 1
            l, r = l + 1, r - 1
            level = level + 1

    def rotate1(self, matrix: List[List[int]]) -> None:
        level = 0
        n = len(matrix)

        while level <= n // 2:
            for column in range(level, n - level - 1):
                tmp = matrix[level][column]
                matrix[level][column] = matrix[n - column - 1][level]
                matrix[n - column - 1][level] = matrix[n - level - 1][n - column - 1]
                matrix[n - level - 1][n - column - 1] = matrix[column][n - level - 1]
                matrix[column][n - level - 1] = tmp
            level += 1

    def rotate2(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(0, n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(0, n):
            for j in range(0, n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


if __name__ == "__main__":
    solution = Solution()
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    solution.rotate2(matrix)
    print(matrix)

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        m, n = len(matrix), len(matrix[0])
        ans = [0] * (m * n)

        index = 0
        up, down, left, right = 0, m - 1, 0, n - 1
        while True:
            print(ans)
            for column in range(left, right + 1):
                ans[index] = matrix[up][column]
                index = index + 1
            up = up + 1
            if up > down:
                break

            for row in range(up, down + 1):
                ans[index] = matrix[row][right]
                index = index + 1
            right = right - 1
            if right < left:
                break

            for column in range(right, left - 1, -1):
                ans[index] = matrix[down][column]
                index = index + 1
            down = down - 1
            if down < up:
                break

            for row in range(down, up - 1, -1):
                ans[index] = matrix[row][left]
                index = index + 1
            left = left + 1
            if left > right:
                break

        return ans


if __name__ == "__main__":
    solution = Solution()
    nums = [[2, 5, 8], [4, 0, -1]]
    print(solution.spiralOrder(nums))

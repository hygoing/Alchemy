import copy
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["." for i in range(0, n)] for j in range(0, n)]
        self.dfs(0, n, board, ans)
        return ans

    def dfs(self, row: int, n: int, board: List[List[str]], ans: List[List[str]]):
        if row == n:
            tmp = [""] * n
            for i in range(0, n):
                tmp[i] = "".join(board[i])
            ans.append(tmp)
            return

        for column in range(0, n):
            if not self.isValid(board, row, column, n):
                continue
            board[row][column] = "Q"
            self.dfs(row + 1, n, copy.deepcopy(board), ans)
            board[row][column] = "."

    def isValid(self, board: List[List[str]], row: int, column: int, n: int) -> bool:
        # 判断列
        for i in range(0, row):
            if board[i][column] == "Q":
                return False

        # 检查右上方是否有皇后互相冲突
        r_row, r_col = row, column
        while r_row > 0 and r_col < n - 1:
            r_row -= 1
            r_col += 1
            if board[r_row][r_col] == 'Q':
                return False
        # 检查左上方是否有皇后互相冲突
        l_row, l_col = row, column
        while l_row > 0 and l_col > 0:
            l_row -= 1
            l_col -= 1
            if board[l_row][l_col] == 'Q':
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    ans = solution.solveNQueens(4)
    print("---------------------------------------------------------------------")
    for i in range(0, len(ans)):
        for j in range(0, len(ans[i])):
            print(ans[i][j] + ' ')
        print("-------------------------------------------")

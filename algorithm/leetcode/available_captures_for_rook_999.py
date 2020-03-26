from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ans = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == "R":
                    for k in range(0, 4):
                        x, y = i, j
                        while True:
                            x = x + dx[k]
                            y = y + dy[k]

                            if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]) or board[x][y] == "B":
                                break

                            if board[x][y] == "p":
                                ans = ans + 1
                                break

                    return ans
        return 0

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, columns, nines = {}, {}, {}
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == ".":
                    continue
                row_key = str(i) + str(board[i][j])
                if row_key in rows:
                    return False
                rows[row_key] = 1

                column_key = str(j) + str(board[i][j])
                if column_key in columns:
                    return False
                columns[column_key] = 1

                nine_key = str(i // 3) + str(j // 3) + str(board[i][j])
                if nine_key in nines:
                    return False
                nines[nine_key] = 1

        return True


if __name__ == "__main__":
    s = "" + str(1)
    print(0 // 3, 1 // 3, 2 // 3)

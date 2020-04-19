class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = ""
        tmp_ans = [""] * min(numRows, len(s))

        row = 0
        goto_down = False

        for i in range(0, len(s)):
            tmp_ans[row] += s[i]
            if row == 0 or row == min(numRows, len(s)) - 1:
                goto_down = not goto_down
            add = 1 if goto_down else -1
            row = row + add

        for i in range(0, len(tmp_ans)):
            ans = ans + tmp_ans[i]
        return ans

        str.join()
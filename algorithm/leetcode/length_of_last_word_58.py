class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            if ans == 0 and s[i] == ' ':
                continue
            if ans >0 and s[i] == ' ':
                break
            ans += 1
        return ans
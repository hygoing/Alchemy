class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        tmp = ""
        for i in range(0, len(s)):
            if s[i] != " ":
                tmp = tmp + s[i]
            if s[i] != " " and (i == len(s) - 1 or s[i + 1] == " "):
                stack.append(tmp)
                tmp = ""

        return " ".join(stack)

    def reverseWords2(self, s: str) -> str:
        ans = []
        s = s.strip()
        i, j = len(s) - 1, len(s) - 1

        while j >= 0:
            while j >= 0 and s[j] != " ":
                j = j - 1
            ans.append(s[j + 1:i + 1])
            while s[j] == " ":
                j = j - 1
            i = j
        return " ".join(ans)


if __name__ == "__main__":
    solution = Solution()
    ans = solution.reverseWords2("  hello world!  ")
    print(ans)

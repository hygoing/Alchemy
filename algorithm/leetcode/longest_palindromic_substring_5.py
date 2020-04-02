class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) == 0:
            return s

        curr_length = 1
        max_length = 1
        max_start = 0

        for i in range(0, len(s)):
            l = i - 1
            r = i + 1
            while r < len(s) and s[r] == s[i]:
                r = r + 1
                curr_length = curr_length + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1
                curr_length = curr_length + 2

            if curr_length > max_length:
                max_start = l + 1
                max_length = curr_length

            curr_length = 1

        return s[max_start:max_start + max_length]

    def dp(self, s: str) -> str:
        if s is None or len(s) == 0:
            return s

        dps = [[False for i in range(0, len(s))] for j in range(0, len(s))]
        max_len = 1
        max_start = 0

        for r in range(1, len(s)):
            for l in range(0, r):
                if s[l] == s[r] and (r - l <= 2 or dps[l + 1][r - 1]):
                    dps[l][r] = True
                    if r - l + 1 > max_len:
                        max_len = r - l + 1
                        max_start = l

        return s[max_start:max_start + max_len]


if __name__ == "__main__":
    solution = Solution()
    s = "babadada"
    print(s)
    print(solution.dp(s))

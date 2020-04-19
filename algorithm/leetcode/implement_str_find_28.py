class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        for i in range(0, len(haystack) - len(needle) + 1):
            l = i
            r = 0
            while r < len(needle) and l < len(haystack) and haystack[l] == needle[r]:
                l = l + 1
                r = r + 1
            if r == len(needle):
                return i
        return -1


if __name__ == "__main__":
    s1 = "hello"
    s2 = "lo"
    solution = Solution()
    print(solution.strStr(s1, s2))

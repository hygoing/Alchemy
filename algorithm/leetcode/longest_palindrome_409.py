class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        char_map = {}
        for ch in s:
            char_map[ch] = char_map.get(ch, 0) + 1

        for k, v in char_map.items():
            if v % 2 == 1:
                v = v - 1
            result = result + v

        if result < len(s):
            result = result + 1

        return result

if __name__ == "__main__":
    solution = Solution()
    res = solution.longestPalindrome("abccccdd")
    print(res)
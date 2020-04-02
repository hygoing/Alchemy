class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        ans = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in num_dict:
                ans = ans + num_dict[s[i:i + 2]]
                i = i + 2
            else:
                ans = ans + num_dict[s[i]]
                i = i + 1
        return ans


if __name__ == "__main__":
    s = [1, 2, 3, 4]
    for i in range(0, len(s)):
        if i == 1:
            i = i + 2
        print(s[i])

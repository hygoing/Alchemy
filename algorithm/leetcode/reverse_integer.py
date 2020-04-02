'''给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
'''
import math
import sys


class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31
        ans = 0
        abs_x = int(math.fabs(x))
        while abs_x != 0:
            mod = abs_x % 10
            abs_x = abs_x // 10
            ans = ans * 10 + mod
            if x > 0 and ans > max_int:
                return 0
            if x < 0 and -ans < min_int:
                return 0

        if x < 0:
            ans = -ans
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123))

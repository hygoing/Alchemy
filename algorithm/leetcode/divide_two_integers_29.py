import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        abs_dividend = int(math.fabs(dividend))
        abs_divisor = int(math.fabs(divisor))
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31

        while abs_dividend >= abs_divisor:
            counter = 1
            tmp_abs_divisor = abs_divisor
            while (tmp_abs_divisor << 1) < (abs_dividend):
                counter = counter << 1
                tmp_abs_divisor = tmp_abs_divisor << 1
            abs_dividend = abs_dividend - tmp_abs_divisor
            ans = ans + counter

        ans = -ans if (dividend < 0) ^ (divisor < 0) else ans
        return ans if ans <= max_int and ans >= min_int else max_int


if __name__ == "__main__":
    solution = Solution()
    print(solution.divide(10, 3))

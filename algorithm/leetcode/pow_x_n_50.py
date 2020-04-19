import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 0
        ans = x
        abs_n = int(math.fabs(n))

        level = 1
        while level < abs_n:
            if level << 1 <= abs_n:
                ans = ans * ans
                level <<= 1
            else:
                ans = ans * x
                level = level + 1

        return ans if n > 0 else 1 / ans

    def myPowRecursion(self, x: float, n: int) -> float:
        if n < 0:
            return 1/x
        if n == 0:
            return 1
        if n == 1:
            return x

        ans = self.myPowRecursion(x, n // 2)
        ans *= ans
        if n & 1 == 1:
            ans *= x
        return ans

    def myPowIteration(self, x: float, n: int) -> float:
        if n == 0:
            return 0
        if n == 1:
            return x

        ans = 1
        curr = x
        while n > 0:
            if n & 1 == 1:
                ans *= curr
            curr *= curr
            n = n >> 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.myPowRecursion(2, -2))

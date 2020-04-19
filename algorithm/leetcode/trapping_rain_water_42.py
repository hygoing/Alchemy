from time import sleep
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 1, len(height) - 2
        lmax, rmax = 0, 0
        ans = 0
        for i in range(1, len(height) - 1):
            if height[l - 1] < height[r + 1]:
                lmax = max(lmax, height[l - 1])
                if lmax > height[l]:
                    ans = ans + lmax - height[l]
                l = l + 1
            else:
                rmax = max(rmax, height[r + 1])
                if rmax > height[r]:
                    ans = ans + rmax - height[r]
                r = r - 1
        return ans

    def trapForStack(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(0, len(height)):
            while len(stack) > 0 and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                while len(stack) > 0 and height[stack[-1]] == height[tmp]:
                    stack.pop()

                if len(stack) > 0:
                    l = stack[-1]
                    ans = ans + (min(height[l], height[i]) - height[tmp]) * (i - l - 1)
            stack.append(i)
        return ans

    def trapForStackForDp(self, height: List[int]) -> int:
        ans = 0
        dpl = [0] * len(height)
        dpr = [0] * len(height)

        for i in range(1, len(height)):
            dpl[i] = max(dpl[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            dpr[i] = max(dpr[i + 1], height[i + 1])

        for i in range(1, len(height) - 1):
            hmin = min(dpl[i], dpr[i])
            if hmin > height[i]:
                ans = ans + hmin - height[i]
        return ans


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(solution.trap(nums))

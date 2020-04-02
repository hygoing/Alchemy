class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = [-1] * n
        for i in range(0, n):
            nums[i] = i

        index = 0
        while n > 1:
            index = (index + m - 1) % n
            nums.pop(index)
            n = n - 1

        return nums[0]

    def lastRemainingForMath(self, n: int, m: int) -> int:
        # https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/javajie-jue-yue-se-fu-huan-wen-ti-gao-su-ni-wei-sh/
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + m) % i
        return ans

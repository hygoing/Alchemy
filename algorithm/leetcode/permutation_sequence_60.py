from typing import List


class Solution:
    def factorial(self, n: int, k: int) -> str:
        factorial = [1] * (n + 1)
        for i in range(2, n + 1):
            factorial[i] = i * factorial[i - 1]

        nums = [i for i in range(1, n + 1)]
        ans = ""
        for i in range(1, n + 1):
            j = k // factorial[n - i]
            if k % factorial[n - i] != 0:
                j = j + 1
            ans += str(nums[j - 1])
            nums.pop(j - 1)
            k = k % factorial[n - i]

        return ans

    def getPermutation(self, n: int, k: int) -> str:
        nums = [0] * n
        for i in range(1, n + 1):
            nums[i - 1] = i
        for i in range(1, k):
            self.getNext(nums)

        ans = ""
        for i in range(0, len(nums)):
            ans += str(nums[i])
        return ans

    def getNext(self, nums: List[int]):
        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        if i >= 0:
            while nums[k] <= nums[i]:
                k -= 1
            tmp = nums[i]
            nums[i] = nums[k]
            nums[k] = tmp

        l, r = j, len(nums) - 1
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.factorial(3, 3))

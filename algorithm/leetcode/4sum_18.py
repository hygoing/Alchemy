from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        print(nums)

        for i in range(0, len(nums) - 3):
            dif = target - nums[i]

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                l = j + 1
                r = len(nums) - 1

                if nums[j] > dif:
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                while l < r:
                    sum = nums[j] + nums[l] + nums[r]
                    if sum > dif:
                        r = r - 1
                    elif sum < dif:
                        l = l + 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l = l + 1
                        while l < r and nums[r] == nums[r - 1]:
                            r = r - 1
                        l = l + 1
                        r = r - 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    nums = [1, -2, -5, -4, -3, 3, 3, 5]
    print(solution.fourSum(nums, -11))


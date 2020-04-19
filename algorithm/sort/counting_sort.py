from typing import List

def countingSort(nums: List[int]):
    max = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[max]:
            max = i

    buckets = [0] * (nums[max] + 1)

    for i in range(0, len(nums)):
        buckets[nums[i]] = buckets[nums[i]] + 1

    for i in range(1, len(buckets)):
        buckets[i] = buckets[i] + buckets[i - 1]

    ans = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        j = buckets[nums[i]] - 1
        ans[j] = nums[i]
        buckets[nums[i]] = buckets[nums[i]] - 1

    for i in range(0,len(ans)):
        nums[i] = ans[i]


if __name__ == "__main__":
    l = [2, 5, 2, 3, 1]
    countingSort(l)
    print(l)

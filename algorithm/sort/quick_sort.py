from typing import List


def quickSort(nums: List[int]):
    qs_recursion(nums, 0, len(nums) - 1)


def qs_recursion(nums: List[int], l: int, r: int):
    if l >= r:
        return
    p = partition(nums, l, r)
    qs_recursion(nums, l, p - 1)
    qs_recursion(nums, p + 1, r)


def partition(nums: List[int], l: int, r: int) -> int:
    p = r
    r = r - 1

    while True:
        while l < r and nums[l] < nums[p]:
            l = l + 1
        while l < r and nums[r] > nums[p]:
            r = r - 1
        if l >= r:
            break
        tmp = nums[l]
        nums[l] = nums[r]
        nums[r] = tmp

    tmp = nums[p]
    nums[p] = nums[r]
    nums[r] = tmp

    return r


if __name__ == "__main__":
    nums = [5, 1, 3, 2, 7, 2, 8, 9, 4, 23, 14]
    quickSort(nums)
    print(nums)

from typing import List


def binarySearch(nums: List[int], val: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2  # 防止 l + r 溢出，可以写成 l + (r-l) // 2
        if nums[m] == val:
            return m
        elif nums[m] > val:
            r = m - 1
        else:
            l = m + 1
    return -1


def binarySearchForRecursion(nums: List[int], val: int, l: int, r: int) -> int:
    if l > r:
        return -1
    m = (l + r) // 2
    if nums[m] == val:
        return m
    elif nums[m] > val:
        return binarySearchForRecursion(nums, val, l, m - 1)
    else:
        return binarySearchForRecursion(nums, val, m + 1, r)


# 重复数组查找第一个值等于给定值的元素
def binarySearchForFirst(nums: List[int], val: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == val:
            if m == 0 or nums[m - 1] != val:
                return m
            else:
                r = m - 1
        elif nums[m] > val:
            r = m - 1
        else:
            l = m + 1
    return -1


def binarySearchForFirst2(nums: List[int], val: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + ((r - l)) >> 1
        if nums[m] == val:
            r = m - 1
        elif nums[m] > val:
            r = m - 1
        else:
            l = m + 1

    if l < len(nums) and nums[l] == val:
        return l
    return -1


# 重复数组查找最后一个值等于给定值的元素
def binarySearchForLast(nums: List[int], val: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == val:
            if m == len(nums) - 1 or nums[m + 1] != val:
                return m
            else:
                l = m + 1
        elif nums[m] > val:
            r = m - 1
        else:
            l + m + 1
    return -1


def binarySearchForLast2(nums: List[int], val: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + ((r - l)) >> 1
        if nums[m] == val:
            l = m + 1
        elif nums[m] > val:
            r = m - 1
        else:
            l = m + 1

    if r > -1 and nums[r] == val:
        return r
    return -1


# 数组查找第一个大于等于给定值的元素
def binarySearchForMoreFirst(nums: List[int], val: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] >= val:
            if m == 0 or nums[m - 1] < val:
                return m
            else:
                r = m - 1
        else:
            l = m + 1
    return -1


# 数组查找第一个小于等于给定值的元素
def binarySearchForLessFirst(nums: List[int], val: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] <= val:
            if m == len(nums) - 1 or nums[m + 1] > val:
                return m
            else:
                l = m + 1
        else:
            r = m - 1
    return -1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binarySearch(nums, 10))

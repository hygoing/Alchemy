from typing import List


def mergeSort(nums: List[int]):
    temp_store = [0] * len(nums)
    recursion_sort(nums, 0, len(nums) - 1, temp_store)


def recursion_sort(nums: List[int], left: int, right: int, temp_store: List[int]):
    if left >= right:
        return
    mid = (left + right) // 2
    recursion_sort(nums, left, mid, temp_store)
    recursion_sort(nums, mid + 1, right, temp_store)
    merge(nums, left, mid, right, temp_store)


def merge(nums: List[int], left: int, mid: int, right: int, temp_store: List[int]):
    l_ptr = left
    r_ptr = mid + 1
    pos = left

    while l_ptr <= mid and r_ptr <= right:
        if nums[l_ptr] < nums[r_ptr]:
            temp_store[pos] = nums[l_ptr]
            l_ptr += 1
        else:
            temp_store[pos] = nums[r_ptr]
            r_ptr += 1
        pos += 1

    while l_ptr <= mid:
        temp_store[pos] = nums[l_ptr]
        l_ptr += 1
        pos += 1

    while r_ptr <= right:
        temp_store[pos] = nums[r_ptr]
        r_ptr += 1
        pos += 1

    for i in range(left, pos):
        nums[i] = temp_store[i]


if __name__ == "__main__":
    nums = [4, 1, 6, 4, 12, 67, 23, 57]
    mergeSort(nums)
    print(nums)

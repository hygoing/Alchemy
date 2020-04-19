from typing import List


def heapSort(nums: List[int]):
    n = len(nums)
    for i in range(len(nums) - 1, -1, -1):
        shiftDown(nums, i, n - 1)

    for i in range(len(nums) - 1, 0, -1):
        swap(nums, 0, i)
        shiftDown(nums, 0, i - 1)


def shiftDown(nums: List[int], i: int, n: int):
    child = 2 * i + 1
    while child <= n:
        if child + 1 <= n and nums[child] < nums[child + 1]:
            child = child + 1
        if nums[child] <= nums[i]:
            break
        swap(nums, i, child)
        i = child
        child = 2 * i + 1


def swap(nums: List[int], x: int, y: int):
    tmp = nums[x]
    nums[x] = nums[y]
    nums[y] = tmp

if __name__ == "__main__":
    l = [5,2,3,1]
    heapSort(l)
    print(l)
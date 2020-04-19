'''
和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是O(n log n）的时间复杂度。代价是需要额外的内存空间。

归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。归并排序是一种稳定的排序方法。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。

算法描述
把长度为n的输入序列分成两个长度为n/2的子序列；
对这两个子序列分别采用归并排序；
将两个排序好的子序列合并成一个最终的排序序列。

最佳情况：T(n) = O(n)  最差情况：T(n) = O(nlogn)  平均情况：T(n) = O(nlogn)

稳定排序
'''

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

from typing import List


def bubbleSort(nums: List[int]):
    for i in range(0, len(nums)):
        need_swap = False
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                need_swap = True

        if need_swap == False:
            return


if __name__ == "__main__":
    l = [6, 1, 8, 4, 2, 9, 0, 3, 2]
    bubbleSort(l)
    print(l)

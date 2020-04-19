from typing import List


def bucketSort(nums: List[int]):
    max = -1
    for i in range(0, len(nums)):
        if nums[i] > max:
            max = nums[i]

    buckets = [0] * (max + 1)
    for i in range(0, len(nums)):
        buckets[nums[i]] = buckets[nums[i]] + 1

    j = 0
    for i in range(0, len(buckets)):
        while buckets[i] > 0:
            nums[j] = i
            j = j + 1
            buckets[i] = buckets[i] - 1


def bucketSortForSize(nums: List[int], bucket_size: int):
    min_num, max_num = 2 ** 31 - 1, -2 ** 31
    for i in range(0, len(nums)):
        min_num = min(min_num, nums[i])
        max_num = max(max_num, nums[i])

    bucket_count = (max_num - min_num) // bucket_size + 1
    buckets = [[0 for i in range(0, 0)] for j in range(0, bucket_count)]
    for i in range(0, len(nums)):
        pos = (nums[i] - min_num) // bucket_size
        buckets[pos].append(nums[i])

    for i in range(0, len(buckets)):
        buckets[i].sort()

    k = 0
    for i in range(0, len(buckets)):
        for j in range(0, len(buckets[i])):
            nums[k] = buckets[i][j]
            k = k + 1


if __name__ == "__main__":
    l = [6, 1, 8, 4, 2, 9, 0, 3, 2]
    bucketSortForSize(l, 3)
    print(l)

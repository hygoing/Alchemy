from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        n = len(intervals)
        intervals.sort()
        ans = []

        l, r = intervals[0][0], intervals[0][1]
        for i in range(0, n):
            if r >= intervals[i][0]:
                r = max(r, intervals[i][1])
                l = min(l, intervals[i][0])
            else:
                ans.append([l, r])
                l = intervals[i][0]
                r = intervals[i][1]
            if i == n - 1:
                ans.append([l, r])
        return ans


if __name__ == "__main__":
    solution = Solution()
    intervals = [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]
    print(solution.merge(intervals))

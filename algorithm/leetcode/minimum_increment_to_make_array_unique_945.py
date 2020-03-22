from typing import List

'''
 countor_list = [0] * 80000
        res, repetition = 0, 0
        for i in range(0, len(A)):
            countor_list[A[i]] = countor_list[A[i]] + 1

        for i in range(0, len(countor_list)):
            if countor_list[i] > 1:
                repetition = repetition + countor_list[i] - 1
                res = res - i * (countor_list[i] - 1)
            elif countor_list[i] == 0 and repetition > 0:
                repetition = repetition - 1
                res = res + i
        return result
'''

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        res = 0
        for i in range(1,len(A)):
            if A[i] <= A[i-1]:
                temp = A[i]
                A[i] = A[i-1] + 1
                res = res + A[i] - temp
        return res

if __name__ == "__main__":
    int_list = [1, 2, 2]
    solution = Solution()
    print(solution.minIncrementForUnique(int_list))

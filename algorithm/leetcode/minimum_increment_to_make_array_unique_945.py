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

    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        res =
        for i in range(1,len(A)):0
            if A[i] <= A[i-1]:
                temp = A[i]
                A[i] = A[i-1] + 1
                res = res + A[i] - temp
        return res

    def minIncrementForUnique(self, A: List[int]) -> int:
        # 线性检测 + 路径压缩
        int_list = [-1] * 80000
        res = 0
        for value in A:
            if int_list[value] == -1:
                int_list[value] = value
            else:
                next = int_list[value] + 1
                jump_path = [next]
                while int_list[next] != -1:
                    next = int_list[next] + 1
                    jump_path.append(next)
                jump_path.append(next)

                for i in range(value, next+1):
                    int_list[i] = next
                res = res + next - value

        return res

    def minIncrementForUnique(self, A: List[int]) -> int:
        # 线性检测 + 路径压缩
        int_list = [-1] * 80000
        res = 0
        for value in A:
            next = self.findPos(value, int_list)
            res = res + next - value

        return res

    def findPos(self, key: int, int_list: List[int]) -> int:
        pos_value = int_list[key]
        if pos_value == -1:
            int_list[key] = key
            return key

        post_value = self.findPos(pos_value + 1, int_list)
        int_list[key] = pos_value
        return pos_value
'''

from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # 线性检测 + 路径压缩
        int_list = [-1] * 80000
        res = 0
        for value in A:
            if int_list[value] == -1:
                int_list[value] = value
            else:
                next = int_list[value] + 1
                jump_path = [value, next]

                while int_list[next] != -1:
                    next = int_list[next] + 1
                    jump_path.append(next)
                jump_path.append(next)

                for jump_value in jump_path:
                    int_list[jump_value] = next

                res = res + next - value

        return res


if __name__ == "__main__":
    int_list = [3,1,2,2,1,7]
    solution = Solution()
    print(solution.minIncrementForUnique(int_list))

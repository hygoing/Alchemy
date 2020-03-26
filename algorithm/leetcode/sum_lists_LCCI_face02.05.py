# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''

给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。

示例：
输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：假设这些数位是正向存放的，请再做一遍。

示例：
输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_ptr, l2_ptr = l1, l2

        carry_bit = 0
        l1_last_ptr = None
        while l1_ptr is not None:
            if l1_ptr.next is None:
                l1_last_ptr = l1_ptr

            sum = l1_ptr.val + carry_bit
            if l2_ptr is not None:
                sum = sum + l2_ptr.val
                l2_ptr = l2_ptr.next

            l1_ptr.val = sum % 10
            l1_ptr = l1_ptr.next
            carry_bit = 1 if sum > 9 else 0

        if l2_ptr is not None:
            l1_last_ptr.next = l2_ptr

        while l1_last_ptr.next is not None:
            l1_last_ptr = l1_last_ptr.next

            sum = l1_last_ptr.val + carry_bit
            carry_bit = 1 if sum > 9 else 0
            l1_last_ptr.val = sum % 10

        if carry_bit == 1:
            l1_last_ptr.next = ListNode(1)

        return l1
'''

from algorithm.leetcode.model import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        guard = ListNode(-1)
        ans = guard
        carry_bit = 0

        while l1 or l2:
            if l1 and l2:
                sum = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum = l1.val
                l1 = l1.next
            elif l2:
                sum = l2.val
                l2 = l2.next

            sum = sum + carry_bit
            carry_bit = 1 if sum > 9 else 0

            node = ListNode(sum % 10)
            ans.next = node
            ans = node

        if carry_bit == 1:
            ans.next = ListNode(1)

        return guard.next


if __name__ == "__main__":
    solution = Solution()

    l1 = ListNode(5)
    l2 = ListNode(5)
    #l2.next = ListNode(9)

    ans = solution.addTwoNumbers(l1, l2)
    while ans is not None:
        print(ans.val)
        ans = ans.next

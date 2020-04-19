# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from algorithm.leetcode.model import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        guard = ListNode(0)
        guard.next = head

        pre = guard
        while pre.next is not None and pre.next.next is not None:
            l = pre.next
            r = pre.next.next
            print(l.val,r.val)

            l.next = r.next
            r.next = l
            pre.next = r

            pre = l

        return guard.next

if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4

    l = solution.swapPairs(l1)
    while l is not None:
        print(l.val)
        l = l.next

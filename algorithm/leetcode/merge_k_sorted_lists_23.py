# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List

from algorithm.leetcode.model import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l, r = 0, len(lists) - 1
        while r > 0:
            if l >= r :
                r = l
                l = 0
            lists[l] = self.merge(lists[l], lists[r])
            l = l + 1
            r = r - 1
        return lists[0] if len(lists) > 0 else None

    def merge(self, ll: ListNode, lr: ListNode) -> ListNode:
        guard = ListNode(0)
        lm = guard

        while ll and lr:
            if ll.val < lr.val:
                lm.next = ll
                ll = ll.next
            else:
                lm.next = lr
                lr = lr.next
            lm = lm.next

        if ll:
            lm.next = ll

        if lr:
            lm.next = lr
        return guard.next


if __name__ == "__main__":
    pass

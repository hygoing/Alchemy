# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.

'''
from algorithm.leetcode.model import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        guard = ListNode(-1)
        guard.next = head
        pre, curr = guard, guard
        for i in range(0, n):
            if curr is None:
                return None
            curr = curr.next

        while curr.next is not None:
            pre = pre.next
            curr = curr.next
        pre.next = pre.next.next

        return guard.next

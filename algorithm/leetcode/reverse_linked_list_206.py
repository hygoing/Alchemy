# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''

from algorithm.leetcode.model import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        pre, curr = None, head
        while curr is not None:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        return pre

    def reverseListForHeadInsert(self, head: ListNode) -> ListNode:
        guard = ListNode(-1)
        while head is not None:
            temp = head.next
            head.next = guard.next
            guard.next = head
            head = temp
        return guard.next

    def reverseListForRecursion(self, head: ListNode) -> ListNode:
        ans = self.recursionFunc(head)
        return ans

    def recursionFunc(self, node: ListNode) -> ListNode:
        if node.next is None:
            return node

        head = self.recursionFunc(node.next)
        node.next.next = node
        node.next = None
        return head


if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    solution = Solution()
    head = solution.reverseListForRecursion(node_1)
    while head is not None:
        print(head.val)
        head = head.next

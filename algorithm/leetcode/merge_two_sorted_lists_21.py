# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

'''
from algorithm.leetcode.model import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        guard = ListNode(-1)
        ans = guard
        l1_ptr, l2_ptr = l1, l2

        while l1_ptr is not None and l2_ptr is not None:
            if l1_ptr.val < l2_ptr.val:
                ans.next = l1_ptr
                l1_ptr = l1_ptr.next
            else:
                ans.next = l2_ptr
                l2_ptr = l2_ptr.next
            ans = ans.next

        if l1_ptr is not None:
            ans.next = l1_ptr
        else:
            ans.next = l2_ptr

        return guard.next


if __name__ == "__main__":
    solution = Solution()
    node_1 = ListNode(-9)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2

    node_3.next = node_4

    solution = Solution()
    head = solution.mergeTwoLists(node_1, node_3)
    while head is not None:
        print(head.val)
        head = head.next

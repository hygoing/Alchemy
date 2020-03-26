# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5

'''
from algorithm.leetcode.model import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        ll, lr = self.split(head)
        ll = self.sortList(ll)
        lr = self.sortList(lr)
        return self.conquer(ll, lr)

    def conquer(self, ll: ListNode, lr: ListNode):
        guard = ListNode(-1)
        lm = guard

        while ll is not None and lr is not None:
            if ll.val < lr.val:
                lm.next = ll
                ll = ll.next
            else:
                lm.next = lr
                lr = lr.next
            lm = lm.next

        if ll is not None:
            lm.next = ll
        else:
            lm.next = lr

        return guard.next

    def split(self, node: ListNode):
        slow, fast = node, node.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        l1 = node
        l2 = slow.next
        slow.next = None
        return l1, l2


def stringList(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    node_1 = ListNode(4)
    node_2 = ListNode(1)
    node_3 = ListNode(3)
    node_4 = ListNode(2)
    node_5 = ListNode(7)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    solution = Solution()
    head = solution.sortList(node_1)
    stringList(head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from algorithm.leetcode.model import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            length += 1
        tail.next = head

        step = length - k % length
        for i in range(0, step - 1):
            head = head.next

        ans = head.next
        head.next = None
        return ans


    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head
        sentinel = ListNode(-1)
        sentinel.next = head

        pre = sentinel
        post = sentinel
        length = 0
        while head is not None:
            length += 1
            head = head.next
        k = k % length

        for i in range(0, k):
            post = post.next

        while post.next is not None:
            post = post.next
            pre = pre.next

        post.next = sentinel.next
        sentinel.next = pre.next
        pre.next = None

        return sentinel.next


if __name__ == "__main__":
    l1 = ListNode(0)
    l2 = ListNode(1)
    l3 = ListNode(2)
    l1.next = l2
    l2.next = l3

    solution = Solution()
    l = solution.rotateRight(l1, 1)
    while l is not None:
        print(l.val)
        l = l.next

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。 

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
"""


from algorithm.leetcode.model import Node

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if head is None:
            return None

        cp_head = head
        while cp_head is not None:
            next_node = cp_head.next
            cp_node = Node(cp_head.val, next_node)
            cp_head.next = cp_node
            cp_head = next_node

        l_cp = head.next
        ans = head.next
        while head is not None:
            next_node = l_cp.next
            if l_cp.next is not None:
                l_cp.next = l_cp.next.next
            if head.random is not None:
                l_cp.random = head.random.next
            head = next_node
            l_cp = l_cp.next

        return ans

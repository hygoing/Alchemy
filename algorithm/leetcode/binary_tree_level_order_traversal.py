# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from algorithm.leetcode.model import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        ans, queue = [], [root]

        while len(queue) > 0:
            counter = len(queue)
            temp_ans = []
            while counter > 0:
                curr = queue.pop(0)
                temp_ans.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                counter = counter - 1
            ans.append(temp_ans)

        return ans
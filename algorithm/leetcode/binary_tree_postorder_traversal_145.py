'''
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from algorithm.leetcode.model import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        ans, stack = [], []
        curr = root
        pre = None
        while len(stack) > 0 or curr is not None:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack[-1]
            if curr.right is None or curr.right == pre:
                stack.pop()
                ans.append(curr.val)
                pre = curr
                curr = None
            else:
                curr = curr.right
        return ans

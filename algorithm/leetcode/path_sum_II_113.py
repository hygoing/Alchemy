# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from algorithm.leetcode.model import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        if root is None:
            return ans

        self.dfs(root, sum, ans, [])
        return ans

    def dfs(self, root: TreeNode, sum: int, ans: List[List[int]], tmp_ans: List[int]):
        if root is None:
            return

        tmp_ans.append(root.val)
        if root.left is None and root.right is None and sum == root.val:
            ans.append(tmp_ans.copy())
            tmp_ans.pop()
            return

        self.dfs(root.left, sum - root.val, ans, tmp_ans)
        self.dfs(root.right, sum - root.val, ans, tmp_ans)
        tmp_ans.pop()

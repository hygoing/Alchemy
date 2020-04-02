# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from algorithm.leetcode.model import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        return self.dfs(root, sum)

    def dfs(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return sum == root.val

        return self.dfs(root.left, sum - root.val) or self.dfs(root.right, sum - root.val)

    def bfs(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        path_sums = [root.val]
        stack = [root]

        while len(stack) > 0:
            path_sum = path_sums.pop()
            curr = stack.pop()

            if curr.left is None and curr.right is None and path_sum == sum:
                return True
            if curr.right is not None:
                stack.append(curr.right)
                path_sums.append(path_sum + curr.right.val)
            if curr.left is not None:
                stack.append(curr.left)
                path_sums.append(path_sum + curr.left.val)

        return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''
from algorithm.leetcode.model import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, node: TreeNode, level: int) -> int:
        if node is None:
            return level

        return max(self.dfs(node.left, level + 1), self.dfs(node.right, level + 1))

    def bfs(self, root: TreeNode) -> int:
        if root is None:
            return 0

        level = 0
        queue = [root]

        while len(queue) > 0:
            level = level + 1
            q_size = len(queue)

            while q_size > 0:
                curr = queue.pop(0)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                q_size = q_size - 1
        return level

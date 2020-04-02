# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
'''
from algorithm.leetcode.model import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def dfs(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False

        return (t1.val == t2.val) and self.dfs(t1.left, t2.right) and self.dfs(t1.right, t2.left)

    def bfs(self, root: TreeNode) -> bool:
        if root is None:
            return True

        queue = [root]
        while len(queue) > 0:
            q_size = len(queue)
            nodes = [-1] * q_size
            for i in range(0, q_size):
                curr = queue.pop(0)
                nodes[i] = -1 if curr is None else curr.val
                if curr is not None:
                    queue.append(curr.left)
                    queue.append(curr.right)

            for i in range(0, q_size // 2):
                if nodes[i] != nodes[q_size - i - 1]:
                    return False
        return True

    def bfs(self, root: TreeNode) -> bool:
        stack = [root, root]

        while len(stack) > 0:
            t2 = stack.pop()
            t1 = stack.pop()

            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False

            stack.append(t1.left)
            stack.append(t2.right)
            stack.append(t1.right)
            stack.append(t2.left)

        return True

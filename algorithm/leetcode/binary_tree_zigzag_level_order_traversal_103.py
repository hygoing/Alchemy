'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        ans, queue = [], [root]
        level = True
        while len(queue) > 0:
            counter = len(queue)
            temp_ans = [0] * counter
            while counter > 0:
                curr = queue.pop(0)
                index = len(temp_ans) - counter if level else counter - 1
                temp_ans[index] = curr.val
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                counter = counter - 1
            level = not level
            ans.append(temp_ans)

        return ans

    def zigzagLevelOrderForDfs(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, res, 0)
        return res

    def dfs(self, node: TreeNode, res: List[List[int]], level: int):
        if node is None:
            return

        if len(res) == level:
            res.append([])

        if level % 2 == 0:
            res[level].append(node.val)
        else:
            res[level].insert(0, node.val)

        self.recursion(node.left, res, level + 1)
        self.recursion(node.right, res, level + 1)


if __name__ == "__main__":
    solution = Solution()

    n3 = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)

    n3.left = n9
    n3.right = n20
    n20.left = n15
    n20.right = n7

    print(solution.zigzagLevelOrder(n3))

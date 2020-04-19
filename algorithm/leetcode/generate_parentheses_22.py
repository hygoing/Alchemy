from typing import List

from algorithm.leetcode.model import TreeNode


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        if n == 0:
            return ans
        self.dfs("", n, n, ans)
        return ans

    def dfs(self, s: str, left: int, right: int, ans: List[str]):
        if left == 0 and right == 0:
            ans.append(s)
            return

        if left > right:
            return
        if left > 0:
            self.dfs(s + "(", left - 1, right, ans)
        if right > 0:
            self.dfs(s + ")", left, right - 1, ans)

    def bfs(self, n: int) -> List[str]:
        ans = []
        root = TreeNode("", n, n)
        queue = [root]

        while len(queue) > 0:
            curr = queue.pop(0)
            if curr.left == 0 and curr.right == 0:
                ans.append(curr.val)
            if curr.left > 0:
                node = TreeNode(curr.val + "(", curr.left - 1, curr.right)
                queue.append(node)
            if curr.right > 0 and curr.left < curr.right:
                node = TreeNode(curr.val + ")", curr.left, curr.right - 1)
                queue.append(node)

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.bfs(3))

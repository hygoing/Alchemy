from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        visited = [[False for i in range(0, len(grid[0]))] for j in range(0, len(grid))]
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if not visited[i][j] and grid[i][j] == "1":
                    ans = ans + 1
                    self.dfs(i, j, grid, visited)
                    print(visited)

        return ans

    def dfs(self, i: int, j: int, grid: List[List[str]], visited: List[List[bool]]):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] or grid[i][j] == "0":
            return

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited[i][j] = True

        for k in range(0, 4):
            x = i + dx[k]
            y = j + dy[k]
            self.dfs(x, y, grid, visited)

    def bfs(self, grid: List[List[str]]) -> int:
        if len(grid) < 0 or len(grid[0]) < 0:
            return 0
        ans = 0
        visited = [[False for i in range(0, len(grid[0]))] for j in range(0, len(grid))]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if not visited[i][j] and grid[i][j] == "1":
                    ans = ans + 1
                    visited[i][j] = True
                    queue = [[i, j]]
                    while len(queue) > 0:
                        xy = queue.pop()
                        x = xy[0]
                        y = xy[1]
                        for k in range(0, 4):
                            _x = x + dx[k]
                            _y = y + dy[k]
                            if _x < 0 or _x >= len(grid) or _y < 0 or _y >= len(grid[i]) or visited[_x][_y] or grid[_x][
                                _y] == "0":
                                continue
                            visited[_x][_y] = True
                            queue.append([_x, _y])
        return ans


if __name__ == "__main__":
    solution = Solution()
    nums = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
    print(solution.bfs(nums))

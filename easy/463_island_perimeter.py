from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i == 0 or grid[i - 1][j] == 0:
                    ans += 1
                if i == m - 1 or grid[i + 1][j] == 0:
                    ans += 1
                if j == 0 or grid[i][j - 1] == 0:
                    ans += 1
                if j == n - 1 or grid[i][j + 1] == 0:
                    ans += 1
        return ans


def test_solution():
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    assert Solution().islandPerimeter(grid) == 16

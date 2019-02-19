from collections import deque


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        count = 0
        m, n = len(grid), len(grid[0])

        def dfs(p, q):
            if 0 <= p < m and 0 <= q < n:
                if grid[p][q] != '1':
                    return
                grid[p][q] = '#'
                dfs(p - 1, q)
                dfs(p + 1, q)
                dfs(p, q - 1)
                dfs(p, q + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count


def test_solution():
    # grid = [
    #     ['1', '1', '1', '1', '0'],
    #     ['1', '1', '0', '1', '0'],
    #     ['1', '1', '0', '0', '0'],
    #     ['0', '0', '0', '0', '0'],
    # ]
    # assert Solution().numIslands(grid) == 1

    grid = [
        ['1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '0'],
    ]
    assert Solution().numIslands(grid) == 1

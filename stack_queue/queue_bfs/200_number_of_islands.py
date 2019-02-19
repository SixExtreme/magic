from collections import deque


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        count, queue = 0, deque()
        m, n = len(grid), len(grid[0])

        s = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue.append((i, j))
                    while queue:
                        p, q = queue.popleft()

                        # solution (memory overflow)
                        # grid[p][q] = '2'
                        # if p - 1 >= 0 and grid[p - 1][q] == '1':
                        #     queue.append((p - 1, q))
                        # if p + 1 < m and grid[p + 1][q] == '1':
                        #     queue.append((p + 1, q))
                        # if q - 1 >= 0 and grid[p][q - 1] == '1':
                        #     queue.append((p, q - 1))
                        # if q + 1 < n and grid[p][q + 1] == '1':
                        #     queue.append((p, q + 1))

                        # solution 2
                        if 0 <= p < m and 0 <= q < n and grid[p][q] == '1':
                            grid[p][q] = '2'
                            queue.extend([
                                (p - 1, q), (p + 1, q),
                                (p, q - 1), (p, q + 1)
                            ])
                    count += 1
                    queue.clear()

        return count


def test_solution():
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]
    assert Solution().numIslands(grid) == 1

    grid = [
        ['1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '0'],
    ]
    assert Solution().numIslands(grid) == 1


if __name__ == '__main__':
    test_solution()


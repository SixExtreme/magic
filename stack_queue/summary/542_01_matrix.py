import sys
from collections import deque


class Solution:
    # solution 1
    # def updateMatrix(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
    #     m = len(matrix)
    #     if m == 0:
    #         return []
    #     n = len(matrix[0])
    #     if n == 0:
    #         return []
    #
    #     def BFS(matrix, i, j):
    #         distance = 0
    #         visit, queue = {(i, j)}, deque([(i, j)])
    #         while queue:
    #             size = len(queue)
    #             for _ in range(size):
    #                 x, y = queue.popleft()
    #                 if 0 <= x < m and 0 <= y < n:
    #                     if matrix[x][y] == 0:
    #                         ans[i][j] = distance
    #                         return
    #                     visit.add((x, y))
    #                     queue.extend([
    #                         (x - 1, y), (x + 1, y),
    #                         (x, y - 1), (x, y + 1)
    #                     ])
    #             distance += 1
    #
    #     ans = [[0 for _ in range(n)] for _ in range(m)]
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == 0:
    #                 continue
    #             BFS(matrix, i, j)
    #     return ans

    # solution 2
    def updateMatrix(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        m, n = len(matrix), len(matrix[0])
        directs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        queue = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = sys.maxsize

        while queue:
            x, y = queue.popleft()
            for dx, dy in directs:
                tx, ty = x + dx, y + dy
                if 0 <= tx < m and 0 <= ty < n and matrix[tx][ty] > matrix[x][y] + 1:
                    queue.append((tx, ty))
                    matrix[tx][ty] = matrix[x][y] + 1

        return matrix


def test_solution():
    matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert Solution().updateMatrix(matrix) == matrix

    matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]
    res = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 2, 1]
    ]
    assert Solution().updateMatrix(matrix) == res


if __name__ == '__main__':
    test_solution()




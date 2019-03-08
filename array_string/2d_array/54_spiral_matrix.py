class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        ans = []

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return ans
        m, n = len(matrix), len(matrix[0])

        si, sj = 0, 0
        while si < m and sj < n:
            # left -> right
            for j in range(sj, n):
                ans.append(matrix[si][j])

            # up -> down
            for i in range(si + 1, m - 1):
                ans.append(matrix[i][n - 1])

            # right -> left
            if si != m - 1:
                for j in reversed(range(sj, n)):
                    ans.append(matrix[m - 1][j])

            # down -> up
            if sj != n - 1:
                for i in reversed(range(si + 1, m - 1)):
                    ans.append(matrix[i][sj])

            m, n = m - 1, n - 1
            si, sj = si + 1, sj + 1

        return ans


def test_solution():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ans = Solution().spiralOrder(matrix)
    assert ans == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    matrix = [
        [10, 11, 12, 13],
        [14, 15, 16, 17],
        [18, 19, 20, 21],
        [23, 24, 25, 26]
    ]
    ans = Solution().spiralOrder(matrix)
    assert ans == [
        10, 11, 12, 13,
        17, 21, 26, 25,
        24, 23, 18, 14,
        15, 16, 20, 19
    ]

    matrix = [
        [10, 11, 12, 13],
        [14, 15, 16, 17],
        [18, 19, 20, 21]
    ]
    ans = Solution().spiralOrder(matrix)
    assert ans == [
        10, 11, 12, 13,
        17, 21, 20, 19,
        18, 14, 15, 16
    ]

    matrix = [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18],
        [19, 20, 21]
    ]
    ans = Solution().spiralOrder(matrix)
    assert ans == [
        10, 11, 12,
        15, 18, 21,
        20, 19, 16,
        13, 14, 17
    ]


if __name__ == '__main__':
    test_solution()



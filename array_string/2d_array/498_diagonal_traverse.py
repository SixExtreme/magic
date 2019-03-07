class Solution:
    def findDiagonalOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        ans = []

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return ans
        m, n = len(matrix), len(matrix[0])

        i, j, direct = 0, 0, 1
        while i < m and j < n:
            ans.append(matrix[i][j])

            if direct == 1:
                if i == 0 or j == n - 1:
                    if j == n - 1:
                        i += 1
                    else:
                        j += 1
                    direct = -direct
                    continue
            else:
                if j == 0 or i == m - 1:
                    if i == m - 1:
                        j += 1
                    else:
                        i += 1
                    direct = -direct
                    continue

            i -= direct
            j += direct

        return ans


def test_solution():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ans = Solution().findDiagonalOrder(matrix)
    print(ans)
    assert ans == [1, 2, 4, 7, 5, 3, 6, 8, 9]

    matrix = [
        [1, 2],
        [3, 4]
    ]
    ans = Solution().findDiagonalOrder(matrix)
    print(ans)
    assert ans == [1, 2, 3, 4]


if __name__ == '__main__':
    test_solution()

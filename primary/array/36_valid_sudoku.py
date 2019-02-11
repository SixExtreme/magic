class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # solution 1
        # for i in range(9):
        #     for j in range(9):
        #         if not board[i][j].isdigit():
        #             continue
        #         for k in range(9):
        #             if k != i and board[k][j] == board[i][j]:
        #                 return False
        #             if k != j and board[i][k] == board[i][j]:
        #                 return False
        #         m, n = (i // 3) * 3, (j // 3) * 3
        #         for p in range(m, m + 3):
        #             for q in range(n, n + 3):
        #                 if (p, q) != (i, j) and board[p][q] == board[i][j]:
        #                     return False
        # return True

        # solution 2
        s = set()
        for i in range(9):
            for j in range(9):
                if not board[i][j].isdigit():
                    continue

                row_tag = '{}({})'.format(i, board[i][j])
                if row_tag in s:
                    return False
                s.add(row_tag)

                col_tag = '({}){}'.format(board[i][j], j)
                if col_tag in s:
                    return False
                s.add(col_tag)

                m, n = (i // 3) * 3, (j // 3) * 3
                blk_tag = '{}({}){}'.format(m, board[i][j], n)
                if blk_tag in s:
                    return False
                s.add(blk_tag)
        return True


def test_solution():
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
    assert Solution().isValidSudoku(board)

    board[0][0] = '8'
    assert not Solution().isValidSudoku(board)


if __name__ == '__main__':
    test_solution()

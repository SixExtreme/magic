class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> bool:
        hmap = dict()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                row_key = 'r{}v{}'.format(i, board[i][j])
                if row_key in hmap:
                    return False
                hmap[row_key] = True

                col_key = 'c{}v{}'.format(j, board[i][j])
                if col_key in hmap:
                    return False
                hmap[col_key] = True

                b = (i // 3) * 3 + (j // 3)
                blk_key = 'b{}v{}'.format(b, board[i][j])
                if blk_key in hmap:
                    return False
                hmap[blk_key] = True
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

    board = [
        ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
    assert not Solution().isValidSudoku(board)


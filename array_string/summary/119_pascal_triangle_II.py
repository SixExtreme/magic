class Solution:
    def getRow(self, rowIndex: int) -> 'List[int]':
        ans = [1] * (rowIndex + 1)
        if rowIndex < 2:
            return ans
        for level in range(2, rowIndex + 1):
            for i in range(level - 1, 0, -1):
                ans[i] += ans[i - 1]
        return ans


def test_solution():
    assert Solution().getRow(0) == [1]
    assert Solution().getRow(1) == [1, 1]
    assert Solution().getRow(2) == [1, 2, 1]
    assert Solution().getRow(3) == [1, 3, 3, 1]
    assert Solution().getRow(4) == [1, 4, 6, 4, 1]


if __name__ == '__main__':
    test_solution()

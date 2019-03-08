class Solution:
    def generate(self, numRows: int) -> 'List[List[int]]':
        ans = []
        for lv in range(0, numRows):
            arr = [1] * (lv + 1)
            for i in range(1, lv):
                arr[i] = ans[lv - 1][i] + ans[lv - 1][i - 1]
            ans.append(arr)
        return ans


def test_solution():
    assert Solution().generate(3) == [
        [1],
        [1, 1],
        [1, 2, 1]
    ]
    assert Solution().generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]

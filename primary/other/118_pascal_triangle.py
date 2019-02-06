class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for n in range(0, numRows):
            arr = [0] * (n + 1)
            arr[0], arr[-1] = 1, 1
            for i in range(1, n):
                arr[i] = ans[n-1][i] + ans[n-1][i-1]
            ans.append(arr)
        return ans


def test_solution():
    assert Solution().generate(1) == [[1]]
    assert Solution().generate(2) == [[1], [1, 1]]
    assert Solution().generate(3) == [[1], [1, 1], [1, 2, 1]]
    assert Solution().generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        ans = [0] * len(A)
        i, j = 0, len(A) - 1

        p = len(A) - 1
        while i <= j:
            if abs(A[i]) > abs(A[j]):
                ans[p] = A[i] * A[i]
                i += 1
            else:
                ans[p] = A[j] * A[j]
                j -= 1
            p -= 1
        return ans


def test_solution():
    A = [-4, -1, 0, 3, 10]
    assert Solution().sortedSquares(A) == [0, 1, 9, 16, 100]

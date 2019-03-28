from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0


def test_solution():
    A = [2, 1, 2]
    assert Solution().largestPerimeter(A) == 5

    A = [1, 2, 1]
    assert Solution().largestPerimeter(A) == 0

    A = [3, 2, 3, 4]
    assert Solution().largestPerimeter(A) == 10

    A = [3, 6, 2, 3]
    assert Solution().largestPerimeter(A) == 8


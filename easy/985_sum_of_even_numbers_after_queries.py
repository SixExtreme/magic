from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sum_even = 0
        for x in A:
            if abs(x) % 2 == 0:
                sum_even += x

        ans = []
        for d, i in queries:
            y = A[i] + d
            if abs(A[i]) % 2 != 0:
                if abs(y) % 2 == 0:
                    sum_even += y
            else:
                if abs(y) % 2 != 0:
                    sum_even -= A[i]
                else:
                    sum_even += (y - A[i])

            A[i] = y
            ans.append(sum_even)

        return ans


def test_solution():
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    assert Solution().sumEvenAfterQueries(A, queries) == [8, 6, 2, 4]

class Solution:
    def repeatedNTimes(self, A: 'List[int]') -> int:
        # solution 1
        for i in range(len(A)):
            if i + 1 < len(A) and A[i] == A[i + 1]:
                return A[i]
            if i + 2 < len(A) and A[i] == A[i + 2]:
                return A[i]
            if i + 3 < len(A) and A[i] == A[i + 3]:
                return A[i]

        # solution 2
        # i, j = 0, len(A) - 1
        # while i < len(A) and j >= 0:
        #     if i + 1 < len(A) and A[i] == A[i + 1]:
        #         return A[i]
        #     if i + 2 < len(A) and A[i] == A[i + 2]:
        #         return A[i]
        #     if i + 3 < len(A) and A[i] == A[i + 3]:
        #         return A[i]
        #     if A[i + 1] == A[i + 2]:
        #         return A[i + 1]
        #     if A[i + 2] == A[i + 3]:
        #         return A[i + 2]
        #     if A[i + 1] == A[i + 3]:
        #         return A[i + 1]
        #     i += 1
        #
        #     if j - 1 >= 0 and A[j] == A[j - 1]:
        #         return A[j]
        #     if j - 2 >= 0 and A[j] == A[j - 2]:
        #         return A[j]
        #     if j - 3 >= 0 and A[j] == A[j - 3]:
        #         return A[j]
        #     if A[j - 1] == A[j - 2]:
        #         return A[j - 1]
        #     if A[j - 2] == A[j - 3]:
        #         return A[j - 2]
        #     if A[j - 1] == A[j - 3]:
        #         return A[j - 1]
        #     j -= 1
        # return A[len(A) - 1]

        # solution 3
        for i in range(len(A) - 3):
            if A[i] == A[i + 1]:
                return A[i]
            if A[i] == A[i + 2]:
                return A[i]
            if A[i] == A[i + 3]:
                return A[i]
            if A[i + 1] == A[i + 2]:
                return A[i + 1]
            if A[i + 1] == A[i + 3]:
                return A[i + 1]
            if A[i + 2] == A[i + 3]:
                return A[i + 2]


def test_solution():
    assert Solution().repeatedNTimes([1, 2, 3, 3]) == 3
    assert Solution().repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2

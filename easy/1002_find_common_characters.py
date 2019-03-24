class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        # solution 1
        # if len(A) == 1:
        #     return list(A[0])
        #
        # p, q = [0] * 26, [0] * 26
        # for c in A[0]:
        #     p[ord(c) - ord('a')] += 1
        #
        # for i in range(1, len(A)):
        #     for c in A[i]:
        #         q[ord(c) - ord('a')] += 1
        #     for j in range(26):
        #         p[j], q[j] = min(p[j], q[j]), 0
        #
        # ans = []
        # for i in range(26):
        #     if p[i] > 0:
        #         c = chr(97 + i)
        #         for _ in range(p[i]):
        #             ans.append(c)
        #
        # return ans

        # solution 2
        from collections import Counter

        ans = Counter(A[0])
        for i in range(1, len(A)):
            ans &= Counter(A[i])
        return list(ans.elements())


def test_solution():
    A = ["bella","label","roller"]
    assert Solution().commonChars(A) == ['e', 'l', 'l']

    A = ["cool","lock","cook"]
    assert Solution().commonChars(A) == ['c', 'o']


if __name__ == '__main__':
    test_solution()

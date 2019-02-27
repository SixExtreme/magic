class Solution:
    def fourSumCount(self, A: 'List[int]', B: 'List[int]', C: 'List[int]', D: 'List[int]') -> 'int':
        m = dict()

        for x in A:
            for y in B:
                s = x + y
                m[s] = m.get(s, 0) + 1

        ans = 0
        for x in C:
            for y in D:
                s = x + y
                ans += m.get(-s, 0)

        return ans



def test_solution():
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    assert Solution().fourSumCount(A, B, C, D) == 2

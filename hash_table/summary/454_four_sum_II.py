class Solution:
    def fourSumCount(self, A: 'List[int]', B: 'List[int]', C: 'List[int]', D: 'List[int]') -> 'int':
        hmap = dict()
        for x in A:
            for y in B:
                s2 = x + y
                hmap[s2] = hmap.get(s2, 0) + 1

        ans = 0
        for p in C:
            for q in D:
                s2 = p + q
                ans += hmap.get(-s2, 0)

        return ans


def test_solution():
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    assert Solution().fourSumCount(A, B, C, D) == 2

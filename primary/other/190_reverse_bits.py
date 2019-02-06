class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        origin = '{0:032b}'.format(n)
        return int(origin[::-1], 2)


def test_solution():
    assert Solution().reverseBits(0) == 0
    assert Solution().reverseBits(43261596) == 964176192
    assert Solution().reverseBits(4294967293) == 3221225471

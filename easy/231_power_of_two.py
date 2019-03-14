class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # solution 1
        return n > 0 and n & (n - 1) == 0

        # solution 2
        return n > 0 and bin(n).count('1') == 1


def test_solution():
    assert Solution().isPowerOfTwo(1)
    assert Solution().isPowerOfTwo(4)
    assert Solution().isPowerOfTwo(8)
    assert not Solution().isPowerOfTwo(218)



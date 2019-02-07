# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >= 5


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                if not isBadVersion(m - 1):
                    return m
                r = m
            else:
                if isBadVersion(m + 1):
                    return m + 1
                l = m + 1
        return l


def test_solution():
    assert Solution().firstBadVersion(50) == 5


if __name__ == '__main__':
    test_solution()

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # def isPrime(x):
        #     for k in range(2, x // 2 + 1):
        #         if x % k == 0:
        #             return False
        #     return True
        #
        # count = 0
        # for x in range(2, n):
        #     if isPrime(x):
        #         count += 1
        # return count

        # count, composite_flags = 0, [False] * n
        # for i in range(2, n):
        #     if not composite_flags[i]:
        #         count += 1
        #
        #         j = 2
        #         while i * j < n:
        #             composite_flags[i * j] = True
        #             j += 1
        # return count

        composite_flags = [False] * n
        for i in range(2, n // 2 + 1):
            for j in range(i, n // i + 1):
                if i * j < n:
                    composite_flags[i * j] = True

        # 双指针法遍历
        count, i, j = 0, 2, n - 1
        while i <= j:
            if i == j and (not composite_flags[i]):
                count += 1
            else:
                if not composite_flags[i]:
                    count += 1
                if not composite_flags[j]:
                    count += 1
            i, j = i + 1, j - 1
        return count


def test_solution():
    n, res = 4, 2
    assert Solution().countPrimes(n) == res

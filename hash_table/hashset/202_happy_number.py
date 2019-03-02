class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # solution 1
        # hset = {n}
        # while n != 1:
        #     s = 0
        #     while n != 0:
        #         s += (n % 10) ** 2
        #         n //= 10
        #     n = s
        #     if n not in hset:
        #         hset.add(n)
        #     else:
        #         return False
        # return True

        # solution 2
        def sum_squares(_n: int):
            _s = 0
            while _n != 0:
                _s += (_n % 10) ** 2
                _n //= 10
            return _s

        slow, fast = n, n
        while True:
            slow = sum_squares(slow)
            fast = sum_squares(fast)
            fast = sum_squares(fast)
            if slow == fast:
                return slow == 1


def test_solution():
    assert Solution().isHappy(19)

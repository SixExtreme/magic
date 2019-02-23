class Solution:
    # solution 1
    # def isHappy(self, n: int) -> bool:
    #     s = set()
    #     while True:
    #         t = 0
    #         while n > 0:
    #             t += (n % 10) ** 2
    #             n //= 10
    #         if t == 1:
    #             return True
    #         if t in s:
    #             return False
    #         n = t
    #         s.add(t)

    # solution 2
    def isHappy(self, n: int) -> bool:

        def sum_squares(x):
            s = 0
            while x > 0:
                s += (x % 10) ** 2
                x //= 10
            return s

        slow, fast = n, n
        while True:
            slow = sum_squares(slow)
            fast = sum_squares(fast)
            fast = sum_squares(fast)
            if slow == fast:
                break
        return slow == 1


def test_solution():
    assert Solution().isHappy(19)

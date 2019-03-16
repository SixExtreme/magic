class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # solution 1
        # i = 1
        # while num > 0:
        #     num -= i
        #     i += 2
        # return num == 0

        # solution 2
        # i, j = 1, num
        # while i <= j:
        #     mid = (i + j) // 2
        #     if mid * mid == num:
        #         return True
        #     elif mid * mid < num:
        #         i = mid + 1
        #     else:
        #         j = mid - 1
        # return False

        # solution 3
        x = num
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num


def test_solution():
    assert Solution().isPerfectSquare(16)
    assert not Solution().isPerfectSquare(18)

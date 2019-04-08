class Solution:
    def mySqrt(self, x: int) -> int:
        # solution 1
        if x <= 1:
            return x
        i, j = 1, x
        while j - i > 1:
            if i * i == x:
                return i
            if j * j == x:
                return j
            mid = i + (j - i) // 2
            mid2 = mid * mid
            if mid2 == x:
                return mid
            elif mid2 < x:
                i = mid
            else:
                j = mid
        return i

        # solution 2 (timeout)
        # t = x
        # while t * t > x:
        #     t = (t + x / t) / 2
        # return int(t)

        # solution 3
        for i in range(x + 1):
            if i * i == x:
                return i
            elif i * i < x < (i + 1) * (i + 1):
                return i


def test_solution():
    assert Solution().mySqrt(0) == 0
    assert Solution().mySqrt(1) == 1
    assert Solution().mySqrt(2) == 1
    assert Solution().mySqrt(3) == 1
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(5) == 2
    assert Solution().mySqrt(6) == 2
    assert Solution().mySqrt(7) == 2
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(9) == 3

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # solution 1
        # for i in range(c + 1):
        #     i2 = i * i
        #     if i2 > c:
        #         break
        #     for j in range(i, c + 1):
        #         j2 = j * j
        #         if i2 + j2 == c:
        #             return True
        #         elif i2 + j2 > c:
        #             break
        # return False

        # solution 2
        import math

        a, b = 0, int(math.sqrt(c))
        while a <= b:
            s = a * a + b * b
            if s == c:
                return True
            elif s < c:
                a += 1
            else:
                b -= 1
        return False


def test_solution():
    assert Solution().judgeSquareSum(5) == True
    assert Solution().judgeSquareSum(4) == True
    assert Solution().judgeSquareSum(3) == False

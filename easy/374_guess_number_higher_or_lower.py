# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0


def guess(num):
    pick = 6
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, n
        while a <= b:
            num = (a + b) // 2
            if guess(num) == 0:
                return num
            elif guess(num) == 1:
                a = num + 1
            elif guess(num) == -1:
                b = num - 1
        return 0


def test_solution():
    assert Solution().guessNumber(10) == 6

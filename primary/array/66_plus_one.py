class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 >= 10:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1, *digits]


def test_solution():
    digits = [1, 2, 3]
    assert Solution().plusOne(digits) == [1, 2, 4]

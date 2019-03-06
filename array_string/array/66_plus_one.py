class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                break
        if i == -1:
            digits[0] = 1
            digits.append(0)
        return digits


def test_solution():
    digits = [1, 2, 3]
    assert Solution().plusOne(digits) == [1, 2, 4]

    digits = [9, 9]
    assert Solution().plusOne(digits) == [1, 0, 0]

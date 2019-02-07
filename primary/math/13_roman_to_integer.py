class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        T = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum = T[s[0]]
        for i in range(1, len(s)):
            sum += T[s[i]]
            if T[s[i]] > T[s[i-1]]:
                sum -= 2 * T[s[i-1]]
        return sum


def test_solution():
    assert Solution().romanToInt('III') == 3
    assert Solution().romanToInt('IV') == 4
    assert Solution().romanToInt('IX') == 9
    assert Solution().romanToInt('MCMXCIV') == 1994

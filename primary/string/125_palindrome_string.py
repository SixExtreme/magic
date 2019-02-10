class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # solution 1
        # if len(s) <= 1:
        #     return True
        # i, j = 0, len(s) - 1
        # while i < j:
        #     if not s[i].isdigit() and not s[i].isalpha():
        #         i += 1
        #         continue
        #     if not s[j].isdigit() and not s[j].isalpha():
        #         j -= 1
        #         continue
        #     if s[i].lower() != s[j].lower():
        #         return False
        #     i, j = i + 1, j - 1
        # return True

        # solution 2
        s = [c for c in s if c .isalpha() or c.isdigit()]
        if len(s) <= 1:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True


def test_solution():
    s = "A man, a plan, a canal: Panama"
    assert Solution().isPalindrome(s)

    s = "race a car"
    assert not Solution().isPalindrome(s)


if __name__ == '__main__':
    test_solution()



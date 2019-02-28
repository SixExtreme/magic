class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isdigit() and not s[i].isalpha():
                i += 1
                continue
            if not s[j].isdigit() and not s[j].isalpha():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True


def test_solution():
    assert not Solution().isPalindrome("race a car")
    assert Solution().isPalindrome("A man, a plan, a canal: Panama")


if __name__ == '__main__':
    test_solution()

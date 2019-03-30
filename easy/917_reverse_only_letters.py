class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # solution 1
        chars = list(S)
        i, j = 0, len(chars) - 1
        while i < j:
            if not chars[i].isalpha():
                i += 1
                continue
            if not chars[j].isalpha():
                j -= 1
                continue
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
        return ''.join(chars)


def test_solution():
    S = 'ab-cd'
    assert Solution().reverseOnlyLetters(S) == 'dc-ba'

    S = 'a-bC-dEf-ghIj'
    assert Solution().reverseOnlyLetters(S) == 'j-Ih-gfE-dCba'

    S = 'Test1ng-Leet=code-Q!'
    assert Solution().reverseOnlyLetters(S) == 'Qedo1ct-eeLg=ntse-T!'


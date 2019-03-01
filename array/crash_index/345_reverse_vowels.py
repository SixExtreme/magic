class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        i, j = 0, len(chars) - 1
        while i < j:
            if chars[i].lower() not in vowels:
                i += 1
                continue
            if chars[j].lower() not in vowels:
                j -= 1
                continue
            chars[i], chars[j] = chars[j], chars[i]
            i, j = i + 1, j - 1

        return ''.join(chars)


def test_solution():
    assert Solution().reverseVowels('hello') == 'holle'
    assert Solution().reverseVowels('leetcode') == 'leotcede'

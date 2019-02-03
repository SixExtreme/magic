class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        # for i in range(len(s) // 2):
        #     s[i], s[-i-1] = s[-i-1], s[i]

        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1


def test_solution():
    s = ['h', 'e', 'l', 'l', 'o']
    r = ['o', 'l', 'l', 'e', 'h']
    Solution().reverseString(s)
    assert s == r

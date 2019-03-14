class Solution:
    def countSegments(self, s: str) -> int:
        # solution 1
        # ans = 0
        # for i, ch in enumerate(s):
        #     if ch != ' ' and (i == 0 or s[i - 1] == ' '):
        #         ans += 1
        # return ans

        # solution 2
        ans = 0
        for word in s.strip().split(' '):
            if len(word) > 0:
                ans += 1
        return ans


def test_solution():
    s = "Hello, my name is John"
    assert Solution().countSegments(s) == 5
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # solution 1
        # stack = []
        # for c in s:
        #     if c.isdigit():
        #         if stack and stack[-1].isdigit():
        #             stack[-1] += c
        #         else:
        #             stack.append(c)
        #     elif c.isalpha():
        #         if stack and stack[-1].isalpha():
        #             stack[-1] += c
        #         else:
        #             stack.append(c)
        #     elif c == '[':
        #         stack.append(c)
        #     elif c == ']':
        #         tmp = []
        #         while stack:
        #             peek = stack.pop()
        #             if peek == '[':
        #                 break
        #             tmp.append(peek)
        #         tmp.reverse()
        #         cnt = int(stack.pop())
        #         stack.append(cnt * ''.join(tmp))
        # return ''.join(stack)

        # solution 2
        ans = ''
        cstk, estk = [], []

        i = 0
        while i < len(s):
            if s[i].isdigit():
                cnt = 0
                while i < len(s) and s[i].isdigit():
                    cnt = cnt * 10 + int(s[i])
                    i += 1
                cstk.append(cnt)
            elif s[i] == '[':
                estk.append(ans)
                ans = ''
                i += 1
            elif s[i] == ']':
                cnt = cstk.pop()
                pre = [estk.pop()]
                for _ in range(cnt):
                    pre.append(ans)
                ans = ''.join(pre)
                i += 1
            else:
                ans += s[i]
                i += 1
        return ans


def test_solution():
    s = '3[a]2[bc]'
    assert Solution().decodeString(s) == 'aaabcbc'

    s = '3[a2[c]]'
    assert Solution().decodeString(s) == 'accaccacc'

    s = '2[abc]3[cd]ef'
    assert Solution().decodeString(s) == 'abcabccdcdcdef'

    s = '10[c]'
    assert Solution().decodeString(s) == 'cccccccccc'

    s = '3[z]2[2[y]pq4[2[jk]e1[f]]]ef'
    assert Solution().decodeString(s) == 'zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef'


if __name__ == '__main__':
    test_solution()

class Solution:
    def countAndSay(self, n: 'int') -> 'str':
        # solution 1
        ans = '1'
        for _ in range(1, n):
            n, nums = len(ans), []
            cnt, pre = 1, ans[0]
            for i in range(1, len(ans)):
                if ans[i] == pre:
                    cnt += 1
                else:
                    nums.append('{}{}'.format(cnt, pre))
                    cnt, pre = 1, ans[i]
            else:
                nums.append('{}{}'.format(cnt, pre))
            ans = ''.join(nums)
        return ans


def test_solution():
    assert Solution().countAndSay(1) == '1'
    assert Solution().countAndSay(2) == '11'
    assert Solution().countAndSay(3) == '21'
    assert Solution().countAndSay(4) == '1211'
    assert Solution().countAndSay(5) == '111221'


if __name__ == '__main__':
    test_solution()

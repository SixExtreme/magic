class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # solution 1
        # return bin(int(a, 2) + int(b, 2))[2:]

        # solution 2
        # def add(a: str, b: str, c: str) -> (str, str):
        #     res = 0
        #     if a == '1':
        #         res += 1
        #     if b == '1':
        #         res += 1
        #     if c == '1':
        #         res += 1
        #     if res == 0:
        #         return '0', '0'
        #     if res == 1:
        #         return '1', '0'
        #     if res == 2:
        #         return '0', '1'
        #     if res == 3:
        #         return '1', '1'
        #
        # if len(a) < len(b):
        #     a, b = b, a
        # ans, cry = [], '0'
        # for i in range(-1, -len(a)-1, -1):
        #     if -i > len(b):
        #         bit, cry = add(a[i], '0', cry)
        #     else:
        #         bit, cry = add(a[i], b[i], cry)
        #     ans.append(bit)
        # if cry != '0':
        #     ans.append(cry)
        # return ''.join(reversed(ans))

        # solution 3
        ans, carry = [], 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            _sum = 0
            if i >= 0:
                _sum += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                _sum += ord(b[j]) - ord('0')
                j -= 1
            _sum += carry
            carry = 0 if _sum < 2 else 1
            ans.append('0' if _sum % 2 == 0 else '1')
        if carry > 0:
            ans.append('1')
        return ''.join(reversed(ans))


def test_solution():
    assert Solution().addBinary('10', '10') == '100'
    assert Solution().addBinary('111', '111') == '1110'
    assert Solution().addBinary('1111', '111') == '10110'


if __name__ == '__main__':
    test_solution()

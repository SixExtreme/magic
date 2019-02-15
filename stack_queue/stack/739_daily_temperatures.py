class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # solution 1
        # stk, ans = [], [0] * len(T)
        # for i in range(len(T)):
        #     while stk and T[i] > T[stk[-1]]:
        #         t = stk.pop()
        #         ans[t] = i - t
        #     stk.append(i)
        # return ans

        # solution 2
        ans = [0] * len(T)
        top, stk = -1, [0] * len(T)
        for i in range(len(T)):
            while top > -1 and T[i] > T[stk[top]]:
                ans[stk[top]] = i - stk[top]
                top -= 1
            top += 1
            stk[top] = i
        return ans


def test_solution():
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    assert Solution().dailyTemperatures(temperatures) == [1, 1, 4, 2, 1, 1, 0, 0]


if __name__ == '__main__':
    test_solution()

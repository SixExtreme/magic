class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution 1
        # n = len(nums)
        #
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums)
        #
        # dp = [0] * n
        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # for i in range(2, n):
        #     dp[i] = max(dp[i-2] + nums[i], dp[i - 1])
        # return dp[n-1]

        # solution 2
        # n = len(nums)
        #
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return nums[0]
        #
        # dp0, dp1 = max(nums[0], nums[1]), nums[0]
        # for i in range(2, n):
        #     dp1, dp2 = dp0, dp1
        #     dp0 = max(dp2 + nums[i], dp1)
        # return dp0

        # solution 3
        # this is an
        dp1, dp2 = 0, 0
        for x in nums:
            dp1 = max(dp1 + x, dp2)
            dp1, dp2 = dp2, dp1
        return dp2


def test_solution():
    assert Solution().rob([1, 2, 3, 1]) == 4
    assert Solution().rob([2, 7, 9, 3, 1]) == 12

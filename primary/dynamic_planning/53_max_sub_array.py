class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) == 0:
        #     return 0
        # sum, max_sum = nums[0], nums[0]
        # for i in range(1, len(nums)):
        #     sum = max(sum + nums[i], nums[i])
        #     max_sum = max(max_sum, sum)
        # return max_sum

        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)


def test_solution():
    nums, res = [-2, 1, -3, 4, -1, 2, 1, -5, 4], 6
    assert Solution().maxSubArray(nums) == res

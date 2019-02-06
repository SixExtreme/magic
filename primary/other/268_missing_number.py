class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (n + 1) * n // 2 - sum(nums)


def test_solution():
    nums = [3, 0, 1]
    assert Solution().missingNumber(nums) == 2

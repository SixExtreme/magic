class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans


def test_solution():
    nums = [1, 1, 2, 3, 3, 4, 4]
    assert Solution().singleNumber(nums) == 2

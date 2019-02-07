class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # map = dict()
        # i, j = 0, len(nums) - 1
        # while i <= j:
        #     if i == j:
        #         if nums[i] in map:
        #             return True
        #     else:
        #         if nums[i] in map:
        #             return True
        #         else:
        #             map[nums[i]] = True
        #
        #         if nums[j] in map:
        #             return True
        #         else:
        #             map[nums[j]] = True
        #     i, j = i + 1, j - 1
        # return False

        # map = dict()
        # for x in nums:
        #     if x in map:
        #         return True
        #     else:
        #         map[x] = True
        # return False

        return len(set(nums)) != len(nums)


def test_solution():
    nums = [0, 1, 1, 2, 3]
    assert Solution().containsDuplicate(nums)

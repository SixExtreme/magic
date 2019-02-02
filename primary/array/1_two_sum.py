class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return None

        map = dict()
        for i, num in enumerate(nums):
            if num in map:
                return [map[num], i]
            else:
                map[target - num] = i


def test_solution():
    nums = [2, 7, 11, 15]
    assert Solution().twoSum(nums, 9) == [0, 1]

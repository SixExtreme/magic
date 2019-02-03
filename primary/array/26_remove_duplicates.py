class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1

        return i + 1


def test_solution():
    nums, res = [1, 1, 2], 2
    assert Solution().removeDuplicates(nums) == res

    nums, res = [0,0,1,1,1,2,2,3,3,4], 5
    assert Solution().removeDuplicates(nums) == res

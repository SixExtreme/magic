class Solution:
    # solution 1
    # def moveZeroes(self, nums: 'List[int]') -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     i = 0
    #     while i < len(nums):
    #         if nums[i] != 0:
    #             i += 1
    #         else:
    #             j = i + 1
    #             while j < len(nums) and nums[j] == 0:
    #                 j += 1
    #             if j < len(nums):
    #                 nums[i], nums[j] = nums[j], nums[i]
    #             else:
    #                 break
    #     for k in range(i, len(nums)):
    #         nums[k] = 0

    # solution 2
    # def moveZeroes(self, nums: 'List[int]') -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     i = 0
    #     for j in range(len(nums)):
    #         if nums[j] != 0:
    #             nums[i] = nums[j]
    #             i += 1
    #     while i < len(nums):
    #         nums[i] = 0
    #         i += 1

    # solution 3
    def moveZeroes(self, nums: 'List[int]') -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                continue
            nums[i], nums[j] = nums[j], nums[i]
            i += 1


def test_solution():
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]


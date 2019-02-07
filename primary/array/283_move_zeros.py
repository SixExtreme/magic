class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # i, n = 0, len(nums)
        # while i < n:
        #     if nums[i] != 0:
        #         i += 1
        #     else:
        #         j = i + 1
        #         while j < n and nums[j] == 0:
        #             j += 1
        #         if j < n:
        #             nums[i], nums[j] = nums[j], nums[i]
        #         else:
        #             return

        i = 0
        for x in nums:
            if x != 0:
                nums[i] = x
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1


def test_solution():
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]


if __name__ == '__main__':
    test_solution()

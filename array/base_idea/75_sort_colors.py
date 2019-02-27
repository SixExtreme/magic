class Solution:
    # solution 1
    # def sortColors(self, nums: 'List[int]') -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     p, i, j = 0, 0, len(nums) - 1
    #     while i < j and p <= j:
    #         if nums[p] == 0:
    #             nums[p], nums[i] = nums[i], nums[p]
    #             i += 1
    #             p += 1
    #         elif nums[p] == 2:
    #             nums[p], nums[j] = nums[j], nums[p]
    #             j -= 1
    #         else:
    #             p += 1

    # solution 2
    # def sortColors(self, nums: 'List[int]') -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     p, i, j = 0, 0, len(nums) - 1
    #     while p <= j:
    #         while p < j and nums[p] == 2:
    #             nums[p], nums[j] = nums[j], nums[p]
    #             j -= 1
    #         while p > i and nums[p] == 0:
    #             nums[p], nums[i] = nums[i], nums[p]
    #             i += 1
    #         p += 1

    # solution 3
    # def sortColors(self, nums: 'List[int]') -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     p, i, j = 0, 0, len(nums) - 1
    #     while i < j and p <= j:
    #         if nums[p] == 0:
    #             nums[p], nums[i] = nums[i], nums[p]
    #             i += 1
    #         if nums[p] == 2:
    #             nums[p], nums[j] = nums[j], nums[p]
    #             j -= 1
    #         if p < i or nums[p] == 1:
    #             p += 1

    # solution 4
    def sortColors(self, nums: 'List[int]') -> None:
        i, j = 0, 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1


def test_solution():
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    nums = [2, 0, 1]
    Solution().sortColors(nums)
    assert nums == [0, 1, 2]


if __name__ == '__main__':
    test_solution()

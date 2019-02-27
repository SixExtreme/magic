class Solution:
    # solution 1
    # def removeDuplicates(self, nums: 'List[int]') -> int:
    #     if len(nums) < 2:
    #         return len(nums)
    #     i = 0
    #     for j in range(1, len(nums)):
    #         if nums[j] == nums[i]:
    #             if i == 0 or nums[i - 1] != nums[j]:
    #                 nums[i + 1] = nums[j]
    #                 i += 1
    #             continue
    #         nums[i + 1] = nums[j]
    #         i += 1
    #     return i + 1

    # solution 2
    # def removeDuplicates(self, nums: 'List[int]') -> int:
    #     i = 0
    #     for x in nums:
    #         if i < 2 or x > nums[i - 2]:
    #             nums[i] = x
    #             i += 1
    #     return i

    # solution 3
    def removeDuplicates(self, nums: 'List[int]') -> int:
        if len(nums) < 2:
            return len(nums)
        i = 0
        for j in range(1, len(nums)):
            if i == 0 or nums[i - 1] != nums[i] or nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1


def test_solution():
    # nums = [1, 1, 1, 2, 2, 3]
    # assert Solution().removeDuplicates(nums) == 5
    # assert nums[0] == 1
    # assert nums[1] == 1
    # assert nums[2] == 2
    # assert nums[3] == 2
    # assert nums[4] == 3

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    assert Solution().removeDuplicates(nums) == 7
    assert nums[0] == 0
    assert nums[1] == 0
    assert nums[2] == 1
    assert nums[3] == 1
    assert nums[4] == 2
    assert nums[5] == 3
    assert nums[6] == 3


if __name__ == '__main__':
    test_solution()

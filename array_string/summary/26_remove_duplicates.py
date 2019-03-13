from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1


def test_solution():
    nums = [1, 1, 2]
    assert Solution().removeDuplicates(nums) == 2

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert Solution().removeDuplicates(nums) == 5

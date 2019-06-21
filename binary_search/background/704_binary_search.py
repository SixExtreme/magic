from typing import List


class Solution:

    @staticmethod
    def search(nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
        return -1


def test_solution():
    nums, target = [5], 5
    assert Solution().search(nums, target) == 0

    nums, target = [-1, 0, 3, 5, 9, 12], 9
    assert Solution().search(nums, target) == 4

    nums, target = [-1, 0, 3, 5, 9, 12], 2
    assert Solution().search(nums, target) == -1

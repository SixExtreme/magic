from typing import List


class Solution:

    # @staticmethod
    # def search(nums: List[int], target: int) -> int:
    #     if len(nums) == 0:
    #         return -1
    #
    #     i, j = 0, len(nums) - 1
    #     while i < j:
    #         mid = i + (j - i) // 2
    #         if nums[mid] > nums[j]:
    #             i = mid + 1
    #         else:
    #             j = mid
    #
    #     base = i
    #     i, j = 0, len(nums) - 1
    #     while i <= j:
    #         k = i + (j - i) // 2
    #         mid = (k + base) % len(nums)
    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid] > target:
    #             j = mid - 1
    #         else:
    #             i = mid + 1
    #
    #     return -1

    @staticmethod
    def search(nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        i, j = 0, n - 1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[i] <= nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return i if nums[i] == target else -1

def test_solution():
    nums, target = [5], 5
    assert Solution().search(nums, target) == 0

    nums, target = [-1, 0, 3, 5, 9, 12], 9
    assert Solution().search(nums, target) == 4

    nums, target = [-1, 0, 3, 5, 9, 12], 2
    assert Solution().search(nums, target) == -1

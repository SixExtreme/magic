class Solution:
    def rotate(self, nums: 'List[int]', k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return
        nums.reverse()

        i, j = 0, k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

        i, j = k, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1


def test_solution():
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 1)
    assert nums == [7, 1, 2, 3, 4, 5, 6]


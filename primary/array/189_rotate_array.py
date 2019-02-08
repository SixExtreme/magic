class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        # solution 1
        # n = len(nums)
        # k %= len(nums)
        # if k == 0:
        #     return
        #
        # extend = [*nums, *nums]
        # i, j = 0, n - k
        # while i < n:
        #     nums[i] = extend[j]
        #     i, j = i + 1, j + 1

        # solution 2 --time out
        # n = len(nums)
        #
        # k %= n
        # if k == 0:
        #     return
        #
        # for _ in range(k):
        #     t = nums[-1]
        #     for i in range(n - 1, 0, -1):
        #         nums[i] = nums[i-1]
        #     nums[0] = t

        # solution 3
        n = len(nums)
        k %= n
        if k == 0:
            return

        i, j = 0, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

        i, j = 0, k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

        i, j = k, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1


def test_solution():
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

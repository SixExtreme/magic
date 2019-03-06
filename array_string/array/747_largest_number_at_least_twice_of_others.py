class Solution:
    def dominantIndex(self, nums: 'List[int]') -> int:
        # solution 1
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        max1, max2 = 0, 1
        if nums[max1] < nums[max2]:
            max1, max2 = max2, max1
        for i in range(2, len(nums)):
            if nums[i] > nums[max1]:
                max1, max2 = i, max1
            elif nums[max1] > nums[i] > nums[max2]:
                max2 = i
        if nums[max1] >= 2 * nums[max2]:
            return max1
        return -1


def test_solution():
    nums = [3, 6, 1, 0]
    assert Solution().dominantIndex(nums) == 1

    nums = [1, 2, 3, 4]
    assert Solution().dominantIndex(nums) == -1

    nums = [1, 0]
    assert Solution().dominantIndex(nums) == 0


if __name__ == '__main__':
    test_solution()

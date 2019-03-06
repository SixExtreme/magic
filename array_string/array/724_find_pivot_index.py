class Solution:
    def pivotIndex(self, nums: 'List[int]') -> int:
        lsum, rsum = 0, sum(nums)
        for i, x in enumerate(nums):
            if lsum == rsum - x:
                return i
            lsum += x
            rsum -= x
        return -1


def test_solution():
    nums = [1, 7, 3, 6, 5, 6]
    assert Solution().pivotIndex(nums) == 3

    nums = [1, 2, 3]
    assert Solution().pivotIndex(nums) == -1

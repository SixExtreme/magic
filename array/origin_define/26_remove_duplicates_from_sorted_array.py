class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> int:
        if len(nums) < 2:
            return len(nums)
        i = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            nums[i + 1] = nums[j]
            i += 1
        return i + 1


def test_solution():
    nums = [1, 1, 2]
    assert Solution().removeDuplicates(nums) == 2
    assert nums[0] == 1
    assert nums[1] == 2

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert Solution().removeDuplicates(nums) == 5
    assert nums[0] == 0
    assert nums[1] == 1
    assert nums[2] == 2
    assert nums[3] == 3
    assert nums[4] == 4

class Solution:
    def removeElement(self, nums: 'List[int]', val: int) -> int:
        i = 0
        for j, x in enumerate(nums):
            if nums[j] == val:
                continue
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        return i


def test_solution():
    nums, val = [3, 2, 2, 3], 3
    assert Solution().removeElement(nums, val) == 2
    assert nums[0] == 2
    assert nums[1] == 2

    nums, val = [0, 1, 2, 2, 3, 0, 4, 2], 2
    assert Solution().removeElement(nums, val) == 5
    assert nums[0] == 0
    assert nums[1] == 1
    assert nums[2] == 3
    assert nums[3] == 0
    assert nums[4] == 4

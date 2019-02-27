class Solution:
    def containsDuplicate(self, nums) -> bool:
        s = set()
        for x in nums:
            if x in s:
                return True
            s.add(x)
        return False


def test_solution():
    nums = [1, 2, 3]
    assert not Solution().containsDuplicate(nums)

    nums = [1, 1, 2, 3]
    assert Solution().containsDuplicate(nums)

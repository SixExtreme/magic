class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        hset = set()
        for x in nums:
            if x in hset:
                return True
            hset.add(x)
        return False


def test_solution():
    nums = [1, 2, 3]
    assert not Solution().containsDuplicate(nums)

    nums = [1, 1, 2, 3]
    assert Solution().containsDuplicate(nums)

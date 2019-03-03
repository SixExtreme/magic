class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        hmap = dict()
        for i, x in enumerate(nums):
            if x in hmap:
                return [hmap[x], i]
            hmap[target - x] = i
        return list()


def test_solution():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]

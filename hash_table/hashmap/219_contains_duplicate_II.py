class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: int) -> bool:
        hset = set()
        for i, x in enumerate(nums):
            if x in hset:
                return True
            hset.add(x)
            if len(hset) > k:
                hset.remove(nums[i - k])
        return False

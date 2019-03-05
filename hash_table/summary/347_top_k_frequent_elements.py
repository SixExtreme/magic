class Solution:
    def topKFrequent(self, nums: 'List[int]', k: int) -> 'List[int]':
        hmap = dict()
        for x in nums:
            hmap[x] = hmap.get(x, 0) + 1

        buckets = [None] * len(nums)
        for num, cnt in hmap.items():
            if buckets[cnt - 1] is None:
                buckets[cnt - 1] = []
            buckets[cnt - 1].append(num)

        ans = []
        for bucket in reversed(buckets):
            if bucket is None:
                continue
            ans.extend(bucket)
            if len(ans) >= k:
                break
        return ans


def test_solution():
    nums = [1, 1, 1, 2, 2, 3]
    assert Solution().topKFrequent(nums, 2) == [1, 2]

    nums = [1]
    assert Solution().topKFrequent(nums, 1) == [1]

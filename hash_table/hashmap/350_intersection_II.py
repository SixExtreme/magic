class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        ans, hmap = [], dict()
        for x in nums1:
            hmap[x] = hmap.get(x, 0) + 1
        for x in nums2:
            if hmap.get(x, 0) > 0:
                hmap[x] -= 1
                ans.append(x)
        return ans


def test_solution():
    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    assert Solution().intersect(nums1, nums2) == [2, 2]

    nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
    assert Solution().intersect(nums1, nums2) == [9, 4]

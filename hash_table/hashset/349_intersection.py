class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # solution 1
        # return list(set(nums1) & set(nums2))

        # solution 2
        ans, hset = set(), set()
        for x in nums1:
            hset.add(x)
        for x in nums2:
            if x in hset:
                ans.add(x)
        return list(ans)


def test_solution():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert set(Solution().intersection(nums1, nums2)) == {2}

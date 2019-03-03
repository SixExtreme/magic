from collections import Counter

class Solution:
    # solution 1
    # def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
    #     c1 = Counter(nums1)
    #     c2 = Counter(nums2)
    #     return list((c1 & c2).elements())

    # solution 2
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = dict()
        for x in nums1:
            m[x] = m.get(x, 0) + 1

        ans = []
        for x in nums2:
            if x in m and m[x] > 0:
                ans.append(x)
                m[x] -= 1
        return ans


def test_solution():
    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    assert Counter(Solution().intersect(nums1, nums2)).get(2) == 2

    nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
    assert Counter(Solution().intersect(nums1, nums2)) == Counter({4: 1, 9: 1})

class Solution:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        # return list(set(nums1) & set(nums2))

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        m, ans = dict(), list()
        for x in nums1:
            m[x] = m.get(x, 0) + 1
        for x in nums2:
            if x in m:
                ans.append(x)
                del m[x]
        return ans


def test_solution():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert set(Solution().intersection(nums1, nums2)) == {2}


if __name__ == '__main__':
    test_solution()

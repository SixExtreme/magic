class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        hmap = dict()
        for s in strs:
            ordered = ''.join(sorted(s))
            if ordered not in hmap:
                hmap[ordered] = []
            hmap[ordered].append(s)
        return list(hmap.values())


def test_solution():
    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    ans = Solution().groupAnagrams(strs)
    assert ans == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

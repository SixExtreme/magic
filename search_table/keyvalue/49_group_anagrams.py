class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        _map = dict()
        for s in strs:
            t = ''.join(sorted(list(s)))
            if t not in _map:
                _map[t] = [s]
            else:
                _map[t].append(s)
        return list(_map.values())


def test_solution():
    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    ans = Solution().groupAnagrams(strs)
    assert ans == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

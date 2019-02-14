class Solution:
    def numSquares(self, n: 'int') -> 'int':
        i, candidates = 1, []
        while i * i <= n:
            candidates.append(i * i)
            i += 1
        if n == candidates[-1]:
            return 1

        level, to_check = 1, {n}
        while to_check:
            rems = set()
            for rem in to_check:
                for c in candidates:
                    if rem == c:
                        return level
                    elif rem < c:
                        break
                    rems.add(rem - c)
            level, to_check = level + 1, rems

        return n


def test_solution():
    assert Solution().numSquares(1) == 1
    # assert Solution().numSquares(12) == 3


if __name__ == '__main__':
    # test_solution()
    print(Solution().numSquares(7168))

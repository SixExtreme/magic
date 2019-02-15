from collections import deque


class Solution:
    def numSquares(self, n: 'int') -> 'int':
        # solution 1
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

        # solution 2
        # candidates, visit = [], [0] * n
        #
        # i = 1
        # while i * i <= n:
        #     candidates.append(i * i)
        #     visit[i * i - 1] = 1
        #     i += 1
        # if candidates[-1] == n:
        #     return 1
        #
        # level, queue = 1, deque(candidates)
        # while queue:
        #     level += 1
        #
        #     count = len(queue)
        #     for _ in range(count):
        #         temp = queue[0]
        #         for c in candidates:
        #             if temp + c == n:
        #                 return level
        #             elif temp + c < n and visit[temp + c - 1] == 0:
        #                 visit[temp + c - 1] = level
        #                 queue.append(temp + c)
        #             elif temp + c > n:
        #                 break
        #         queue.popleft()
        #
        # return n

        # solution 3
        # candidates, visit = [], set()
        #
        # i = 1
        # while i * i <= n:
        #     temp = i * i
        #     candidates.append(temp)
        #     i += 1
        # if n == candidates[-1]:
        #     return 1
        #
        # queue = deque()
        # for c in candidates:
        #     visit.add(c)
        #     queue.append(c)
        #
        # level = 2
        # while queue:
        #     size = len(queue)
        #     for _ in range(size):
        #         front = queue.popleft()
        #         for c in candidates:
        #             temp = front + c
        #             if temp > n:
        #                 break
        #             elif temp == n:
        #                 return level
        #             elif temp < n and temp not in visit:
        #                 visit.add(temp)
        #                 queue.append(temp)
        #     level += 1
        #
        # return n

        # solution 4
        # candidates, visit = [], [0] * n
        # i = 1
        # while i * i <= n:
        #     candidates.append(i * i)
        #     i += 1
        # if candidates[-1] == n:
        #     return 1
        #
        # level = 1
        # visit[n - 1], queue = 1, deque([n])
        # while queue:
        #     size = len(queue)
        #     for _ in range(size):
        #         temp = queue.popleft()
        #         for c in candidates:
        #             if temp - c < 0:
        #                 break
        #             elif temp - c == 0:
        #                 return level
        #             elif temp - c > 0 and visit[temp - c - 1] == 0:
        #                 queue.append(temp - c)
        #                 visit[temp - c - 1] = level
        #     level += 1
        #
        # return n

        # solution 5
        # i, candidates = 1, []
        # while i * i <= n:
        #     candidates.append(i * i)
        #     i += 1
        # if n == candidates[-1]:
        #     return 1
        #
        # level, to_check = 2, set(candidates)
        # while to_check:
        #     nums = set()
        #     for num in to_check:
        #         for c in candidates:
        #             if num + c > n:
        #                 break
        #             elif num + c == n:
        #                 return level
        #             nums.add(num + c)
        #     level, to_check = level + 1, nums
        #
        # return n


def test_solution():
    # assert Solution().numSquares(1) == 1
    assert Solution().numSquares(12) == 3


if __name__ == '__main__':
    test_solution()
    # print(Solution().numSquares(7168))

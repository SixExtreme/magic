from collections import deque


class Solution:
    # solution 1
    # def canVisitAllRooms(self, rooms: 'List[List[int]]') -> 'bool':
    #     count, visit = 0, [0] * len(rooms)
    #
    #     queue = deque([0])
    #     while queue and count < len(rooms):
    #         num = queue.popleft()
    #         if visit[num] == 1:
    #             continue
    #         visit[num], count = 1, count + 1
    #         for key in rooms[num]:
    #             if rooms[key] == 1:
    #                 continue
    #             queue.append(key)
    #
    #     return count == len(rooms)

    # solution 2
    def canVisitAllRooms(self, rooms: 'List[List[int]]') -> 'bool':
        visit, queue = set(), deque([0])

        while queue and len(visit) != len(rooms):
            num = queue.popleft()
            if num in visit:
                continue
            visit.add(num)
            for key in rooms[num]:
                if key in visit:
                    continue
                queue.append(key)

        return len(visit) == len(rooms)


def test_solution():
    rooms = [[1], [2], [3], []]
    assert Solution().canVisitAllRooms(rooms)

    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    assert not Solution().canVisitAllRooms(rooms)


if __name__ == '__main__':
    test_solution()

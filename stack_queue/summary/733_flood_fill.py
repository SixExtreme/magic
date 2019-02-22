from collections import deque


class Solution:
    def floodFill(self, image: 'List[List[int]]', sr: 'int', sc: 'int', new_color: 'int') -> 'List[List[int]]':
        queue = deque([(sr, sc)])

        origin = image[sr][sc]
        image[sr][sc] = new_color

        m, n = len(image), len(image[0])

        while queue:
            x, y = queue.popleft()
            if x > 0 and image[x - 1][y] == origin and image[x - 1][y] != new_color:
                queue.append((x - 1, y))
                image[x - 1][y] = new_color
            if x < m - 1 and image[x + 1][y] == origin and image[x + 1][y] != new_color:
                queue.append((x + 1, y))
                image[x + 1][y] = new_color
            if y > 0 and image[x][y - 1] == origin and image[x][y - 1] != new_color:
                queue.append((x, y - 1))
                image[x][y - 1] = new_color
            if y < n - 1 and image[x][y + 1] == origin and image[x][y + 1] != new_color:
                queue.append((x, y + 1))
                image[x][y + 1] = new_color

        return image


def test_solution():
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    res = [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1]
    ]
    sr, sc, new_color = 1, 1, 2
    assert Solution().floodFill(image, sr, sc, new_color) == res

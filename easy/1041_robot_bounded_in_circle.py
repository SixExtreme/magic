class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # [0, 90, 180, 270] => [right, up, left, down]

        direct = 90
        x, y = 0, 0

        for ch in instructions:
            if ch == 'L':
                direct = (direct + 90 + 360) % 360
            if ch == 'R':
                direct = (direct - 90 + 360) % 360
            if ch == 'G':
                if direct == 0:
                    x += 1
                if direct == 90:
                    y += 1
                if direct == 180:
                    x -= 1
                if direct == 270:
                    y -= 1
        return (x == 0 and y == 0) or (direct != 90)


def test_solution():
    assert Solution().isRobotBounded('GL')
    assert Solution().isRobotBounded('GGLLGG')
    assert not Solution().isRobotBounded('GG')
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def findDuplicateSubtrees(self, root: TreeNode) -> 'List[TreeNode]':
#         ans, hmap = list(), dict()
#         self.DLR(root, hmap, ans)
#         return ans
#
#     def DLR(self, root: TreeNode, hmap: dict, ans: list):
#         if root is None:
#             return '#'
#
#         left = '#'
#         if root.left is not None:
#             left = self.DLR(root.left, hmap, ans)
#         right = '#'
#         if root.right is not None:
#             right = self.DLR(root.right, hmap, ans)
#
#         dlr = '{}{}{}'.format(root.val, left, right)
#         if hmap.get(dlr, 0) == 1:
#             ans.append(root)
#         hmap[dlr] = hmap.get(dlr, 0) + 1
#         return dlr


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> 'List[TreeNode]':
        ans, hmap = [], dict()
        if not root:
            return ans
        queue = deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node is None:
                    continue

                key = self.level_order(node)
                if hmap.get(key, 0) == 1:
                    ans.append(node)
                hmap[key] = hmap.get(key, 0) + 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans

    def level_order(self, root: TreeNode) -> str:
        if not root:
            return '#'
        vals, queue = [], deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if not node:
                    vals.append('#')
                else:
                    vals.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
        return ''.join(vals)


def test_solution():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(4)

    ans = Solution().findDuplicateSubtrees(root)
    vals = [node.val for node in ans]
    assert set(vals) == {2, 4}

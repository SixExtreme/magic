from collections import deque
from typing import List, Deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # solution 1
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans: List[List[int]] = []
        if not root:
            return ans
        queue: Deque[TreeNode] = deque([root])
        while queue:
            vals: List[int] = []
            size: int = len(queue)
            for _ in range(size):
                node = queue.popleft()
                vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(vals)
        return ans

    # solution 2
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     def level(node: TreeNode, depth: int, vals: List[List[int]]):
    #         if not node:
    #             return
    #         if depth >= len(vals):
    #             vals.append([])
    #         vals[depth].append(node.val)
    #         if node.left:
    #             level(node.left, depth + 1, vals)
    #         if node.right:
    #             level(node.right, depth + 1, vals)
    #
    #     ans: List[List[int]] = []
    #     level(root, 0, ans)
    #     return ans




def test_solution():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]

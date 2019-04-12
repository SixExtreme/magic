from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # ans = []
        #
        # if not root:
        #     return ans
        #
        # nodes = [root]
        # i, j = 0, 1
        # while i < j:
        #     level = []
        #     for k in range(i, j):
        #         node = nodes[i]
        #         level.append(node.val)
        #         if node.left:
        #             nodes.append(node.left)
        #             j += 1
        #         if node.right:
        #             nodes.append(node.right)
        #             j += 1
        #         i += 1
        #     ans.append(level)
        # return ans

        ans = []
        if not root:
            return ans

        nodes = deque([root])
        while nodes:
            n, level = len(nodes), list()
            for i in range(n):
                node = nodes.popleft()
                level.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            ans.append(level)
        return ans


def test_solution():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]

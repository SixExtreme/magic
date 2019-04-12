from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        #     return 0
        # else:
        #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # if not root:
        #     return 0
        # depth, queue = 0, deque([root])
        # while queue:
        #     depth += 1
        #     n = len(queue)
        #     for i in range(n):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return depth

        if not root:
            return 0
        depth, queue = 0, [root]

        i, j = 0, 1
        while i < j:
            depth += 1
            n = j
            for i in range(i, n):
                if queue[i].left:
                    queue.append(queue[i].left)
                    j += 1
                if queue[i].right:
                    queue.append(queue[i].right)
                    j += 1
                i += 1

        return depth


def test_solution():
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)
    #
    # assert Solution().maxDepth(root) == 3

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)

    assert Solution().maxDepth(root) == 3

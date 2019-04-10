# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # solution 1
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        value, stack = root.val, [root]
        while stack:
            node: TreeNode = stack.pop()
            if node.val != value:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True

    # def isUnivalTree(self, root: TreeNode) -> bool:
    #     def is_unival(tn: TreeNode, val) -> bool:
    #         if not tn:
    #             return True
    #         if tn.val != val:
    #             return False
    #         return is_unival(tn.left, val) and is_unival(tn.right, val)
    #
    #     if not root:
    #         return True
    #     return is_unival(root, root.val)


def test_solution():
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(1)
    assert Solution().isUnivalTree(root)

    root.val = 2
    assert not Solution().isUnivalTree(root)


if __name__ == '__main__':
    test_solution()

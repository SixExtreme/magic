# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         return self.validateBST(root, -float('inf'), float('inf'))
#
#     def validateBST(self, root, _min, _max):
#         if root is None:
#             return True
#
#         if root.val <= _min or root.val >= _max:
#             return False
#
#         if root.left:
#             if root.left.val >= root.val:
#                 return False
#             elif not self.validateBST(root.left, _min, root.val):
#                 return False
#
#         if root.right:
#             if root.right.val <= root.val:
#                 return False
#             elif not self.validateBST(root.right, root.val, _max):
#                 return False
#
#         return True

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        pre, stack = None, []
        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and root.val <= pre.val:
                return False
            pre, root = root, root.right
        return True


def test_solution():
    root1 = TreeNode(10)
    root1.left = TreeNode(8)
    root1.right = TreeNode(12)
    root1.left.left = TreeNode(7)
    root1.left.right = TreeNode(9)
    root1.right.left = TreeNode(11)
    root1.right.right = TreeNode(13)
    assert Solution().isValidBST(root1)

    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    assert not Solution().isValidBST(root2)

    root2 = TreeNode(10)
    root2.left = TreeNode(5)
    root2.right = TreeNode(15)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(20)
    assert not Solution().isValidBST(root2)


if __name__ == '__main__':
    test_solution()


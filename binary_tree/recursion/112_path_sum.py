# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # solution 1
    # def hasPathSum(self, root: TreeNode, _sum: int) -> bool:
    #     if root is None:
    #         return False
    #     if not root.left and not root.right:
    #         return _sum == root.val
    #     return self.hasPathSum(root.left, _sum - root.val) or self.hasPathSum(root.right, _sum - root.val)

    # solution 2
    def hasPathSum(self, root: TreeNode, _sum: int) -> bool:
        stack, accu = [], 0
        curr, last = root, None
        while curr or stack:
            if curr:
                stack.append(curr)
                accu += curr.val
                curr = curr.left
            else:
                peek = stack[-1]
                if accu == _sum and not peek.left and not peek.right:
                    return True
                if peek.right and peek.right is not last:
                    curr = peek.right
                else:
                    last = stack.pop()
                    accu -= last.val
        return False

    # solution 3
    # def hasPathSum(self, root: TreeNode, _sum: int) -> bool:
    #     if not root:
    #         return False
    #     stack = [(root, root.val)]
    #     while stack:
    #         cur, val = stack.pop()
    #         if not cur.left and not cur.right and val == _sum:
    #             return True
    #         if cur.left:
    #             stack.append((cur.left, val + cur.left.val))
    #         if cur.right:
    #             stack.append((cur.right, val + cur.right.val))
    #     return False

    # solution 4
    # def hasPathSum(self, root: TreeNode, _sum: int) -> bool:
    #     if not root:
    #         return False
    #     stack = [root]
    #     while stack:
    #         curr = stack.pop()
    #         if not curr.left and not curr.right and curr.val == _sum:
    #             return True
    #         if curr.left:
    #             curr.left.val += curr.val
    #             stack.append(curr.left)
    #         if curr.right:
    #             curr.right.val += curr.val
    #             stack.append(curr.right)
    #     return False



def test_solution():
    root = TreeNode(5)

    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)

    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)

    assert Solution().hasPathSum(root, 22)

    assert not Solution().hasPathSum(None, 0)
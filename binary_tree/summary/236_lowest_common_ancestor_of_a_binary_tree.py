from typing import Optional, Set, List, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # solution 1
    # def lowestCommonAncestor(self, root: Optional[TreeNode],
    #                          p: TreeNode,
    #                          q: TreeNode) -> Optional[TreeNode]:
    #     if not root:
    #         return None
    #
    #     map_nodes: Dict[TreeNode, int] = dict()
    #
    #     ip: int = -1
    #     iq: int = -1
    #
    #     stack: List[TreeNode] = []
    #     curr: Optional[TreeNode] = root
    #     while curr or stack:
    #         if curr:
    #             stack.append(curr)
    #             curr = curr.left
    #         else:
    #             curr = stack.pop()
    #             if curr is p:
    #                 ip = len(map_nodes)
    #             if curr is q:
    #                 iq = len(map_nodes)
    #             map_nodes[curr] = len(map_nodes)
    #             curr = curr.right
    #
    #     (il, ir) = (ip, iq) if ip <= iq else (iq, ip)
    #
    #     curr: Optional[TreeNode] = root
    #     while not il < map_nodes[curr] < ir:
    #         if map_nodes[curr] > ir:
    #             curr = curr.left
    #         elif map_nodes[curr] < il:
    #             curr = curr.right
    #         else:
    #             break
    #     return curr

    # solution 2
    # def lowestCommonAncestor(self, root: Optional[TreeNode],
    #                          p: Optional[TreeNode],
    #                          q: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root or root in (p, q):
    #         return root
    #     find_left = self.lowestCommonAncestor(root.left, p, q)
    #     find_right = self.lowestCommonAncestor(root.right, p, q)
    #     return root if find_left and find_right else (find_left or find_right)

    # solution 3
    # def lowestCommonAncestor(self, root: Optional[TreeNode],
    #                          p: Optional[TreeNode],
    #                          q: Optional[TreeNode]) -> Optional[TreeNode]:
    #     stack: List[Optional[TreeNode]] = [root]
    #     map_parent: Dict[Optional[TreeNode], Optional[TreeNode]] = {root: None}
    #     while p not in map_parent or q not in map_parent:
    #         node: Optional[TreeNode] = stack.pop()
    #         if node.left:
    #             map_parent[node.left] = node
    #             stack.append(node.left)
    #         if node.right:
    #             map_parent[node.right] = node
    #             stack.append(node.right)
    #     ancestors: Set[TreeNode] = set()
    #     while p:
    #         ancestors.add(p)
    #         p = map_parent[p]
    #     while q not in ancestors:
    #         q = map_parent[q]
    #     return q

    # solution 4
    def lowestCommonAncestor(self, root: Optional[TreeNode],
                             p: TreeNode,
                             q: TreeNode) -> Optional[TreeNode]:
        def find_path(_root: TreeNode, target: TreeNode):
            pass


def test_solution():
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left
    q = root.right
    assert Solution().lowestCommonAncestor(root, p, q) is root

    q = root.left.right.right
    assert Solution().lowestCommonAncestor(root, p, q) is root.left


if __name__ == '__main__':
    test_solution()

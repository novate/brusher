from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS
        # the longest path has to be between two leaf nodes
        # the longest path is node + longest left + longest right
        self.findMaxPath(root)
        return self.diameter

    def findMaxPath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        l_max = self.findMaxPath(root.left)
        r_max = self.findMaxPath(root.right)

        # update diameter
        self.diameter = max(self.diameter, l_max + r_max)

        return 1 + max(l_max, r_max)

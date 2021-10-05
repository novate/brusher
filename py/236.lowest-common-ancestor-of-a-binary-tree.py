from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRecursive:
    ans = None

    def dfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Tuple[bool, bool]:
        if root is None:
            return False, False
        left_founds = self.dfs(root.left, p, q)
        right_founds = self.dfs(root.right, p, q)

        p_found = left_founds[0] or right_founds[0] or root == p
        q_found = left_founds[1] or right_founds[1] or root == q

        if (p_found and q_found) == False:
            return p_found, q_found
        self.ans = root

        # no going up
        return False, False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.ans


class SolutionBetterRecursive:
    ans = None

    def dfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> int:
        if root is None:
            return 0

        found_num = self.dfs(root.left, p, q) + self.dfs(root.right, p, q)
        if root == p or root == q:
            found_num += 1

        if found_num == 2:
            self.ans = root
            return 0

        return found_num

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.ans

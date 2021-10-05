from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionDFS:
    max_sum = None

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_max = self.dfs(root.left)
        right_max = self.dfs(root.right)
        ans = root.val
        if left_max > 0:
            ans += left_max
        if right_max > 0:
            ans += right_max
        if self.max_sum is None:
            self.max_sum = ans
        else:
            self.max_sum = max(self.max_sum, ans)
        one_path_max = max(left_max, right_max)
        ret = max(one_path_max+root.val, root.val)
        return ret

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_sum

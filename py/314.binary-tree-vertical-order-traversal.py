from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionBFS:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        y_vals = {}
        q = deque()
        q.append((root, 0, 0))
        while q:
            node, x, y = q.popleft()
            if node.left:
                q.append((node.left, x-1, y-1))
            if node.right:
                q.append((node.right, x-1, y+1))
            if y not in y_vals:
                y_vals[y] = []
            y_vals[y].append(node.val)

        sorted_y = sorted(y_vals.keys())
        ans = []
        for y in sorted_y:
            ans.append(y_vals[y])

        return ans

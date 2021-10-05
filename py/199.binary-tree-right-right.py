from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        queue = deque([root])
        new_queue = deque()
        while len(queue) != 0 or len(new_queue) != 0:
            p = queue.popleft()
            if p.left is not None:
                new_queue.append(p.left)
            if p.right is not None:
                new_queue.append(p.right)
            if len(queue) == 0:
                # new level
                ans.append(p.val)
                queue, new_queue = new_queue, queue
        return ans

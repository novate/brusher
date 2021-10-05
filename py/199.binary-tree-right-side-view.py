from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionTwoQueues:
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


class SolutionOneQueueSentinel:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        queue = deque([root, None])
        prev = None
        cur = root
        while len(queue) != 0:
            prev = cur
            cur = queue.popleft()
            while cur is not None:
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                prev = cur
                cur = queue.popleft()

            # meet sentinel, new level will come
            ans.append(prev.val)

            if len(queue) != 0:
                queue.append(None)

        return ans


class SolutionQueueLen:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        queue = deque([root])
        len_level = 1
        new_len_level = 0
        while len(queue) != 0:
            while len_level != 0:
                p = queue.popleft()
                if p.left is not None:
                    queue.append(p.left)
                    new_len_level += 1
                if p.right is not None:
                    queue.append(p.right)
                    new_len_level += 1
                len_level -= 1
                if len_level == 0:
                    ans.append(p.val)
            len_level, new_len_level = new_len_level, len_level

        return ans

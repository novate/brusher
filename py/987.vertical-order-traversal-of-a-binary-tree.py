from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionTwoDict:
    def __init__(self):
        self.x_dict = {}

    def dfs(self, root: Optional[TreeNode], x: int, y: int):
        if root is None:
            return
        if x not in self.x_dict:
            self.x_dict[x] = {}

        if y not in self.x_dict[x]:
            self.x_dict[x][y] = []
        self.x_dict[x][y].append(root.val)
        self.dfs(root.left, x+1, y-1)
        self.dfs(root.right, x+1, y+1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dfs(root, 0, 0)
        sorted_x = sorted(self.x_dict.keys())
        t_dict = {}
        for x in sorted_x:
            for y, v in self.x_dict[x].items():
                if y not in t_dict:
                    t_dict[y] = []
                t_dict[y] += sorted(v)

        sorted_y = sorted(t_dict.keys())
        ans = []
        for y in sorted_y:
            ans.append(t_dict[y])
        return ans

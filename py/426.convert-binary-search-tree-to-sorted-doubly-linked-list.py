class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre_node = None
        self.first_node = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        self.traverse(root)
        self.first_node.left = self.pre_node
        self.pre_node.right = self.first_node
        return self.first_node

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        if self.pre_node:
            root.left = self.pre_node
            self.pre_node.right = root
        else:
            self.first_node = root
        self.pre_node = root
        self.traverse(root.right)

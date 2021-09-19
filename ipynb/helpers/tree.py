from collections import deque


class Node:
    '''An n-ary node.'''
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self) -> str:
        '''Convert a tree to a string of the BFS sequence.'''
        queue = deque([self])
        vals = []
        while queue:
            ptr = queue.popleft()
            if ptr:
                vals.append(str(ptr.val))
                queue.append(ptr.left)
                queue.append(ptr.right)
            else:
                vals.append("null")
        for i in range(len(vals)-1, -1, -1):
            if vals[i] != "null":
                return '[' + ','.join(vals[:i+1]) + ']'
        return "[]"


def string_to_tree_node(input: str) -> TreeNode:
    '''Convert a BFS represented tree string to a tree.'''
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

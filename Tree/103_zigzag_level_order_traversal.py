# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return
        res = []
        q = deque()
        q.append(root)
        zigzag = 0
        while q:
            level = []
            length = len(q)
            for i in range(length):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if zigzag:
                res.append(level[::-1])
                zigzag = 0
            else:
                res.append(level)
                zigzag = 1
        return res
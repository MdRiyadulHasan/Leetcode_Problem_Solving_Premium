# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    def isMirror(self, root_left, root_right):
        if not root_left and not root_right:
            return True
        if not root_left or not root_right:
            return False
        if root_left.val != root_right.val:
            return False
        return self.isMirror(root_left.left, root_right.right) and self.isMirror(root_left.right, root_right.left)
    
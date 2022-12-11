class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        l = self.getCount(root,True)
        r = self.getCount(root,False)
        if l==r:
            return (2**l)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
    def getCount(self,root, isleft):
        count = 0
        while root:
             count+=1
             root = root.left if isleft else root.right
        return count
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    ob = Solution()
    ans = ob.countNodes(root)
    print(ans)
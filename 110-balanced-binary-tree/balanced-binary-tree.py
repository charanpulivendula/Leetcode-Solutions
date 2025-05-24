class Solution:
    def height(self,root):
        if not root:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)
        print(leftheight,rightheight)
        if abs(leftheight-rightheight)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
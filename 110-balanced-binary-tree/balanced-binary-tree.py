# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(root):
            if not root:
                return 0
            return 1+max(height(root.left),height(root.right))

        leftheight = height(root.left)
        rightheight = height(root.right)
        print(leftheight,rightheight)
        if abs(leftheight-rightheight)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
            
        
        
        
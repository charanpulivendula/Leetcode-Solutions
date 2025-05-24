# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def maxpath(root):
            if not root:
                return 0
            nonlocal diameter
            left = maxpath(root.left)
            right = maxpath(root.right)
            diameter = max(diameter,left+right)
            return 1+max(left,right)
        maxpath(root)
        

        return diameter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return 0
        if root:
            left = self.counter(root.left)
        else:
            left = 1

        if left==k-1:
            return root.val
        elif left>k-1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-left-1)
            


    def counter(self,root):
        if not root:
            return 0
        return 1+self.counter(root.left)+self.counter(root.right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        maxindex = float('-inf')
        def traverse(root,index):
            if not root:
                return 0
            right = traverse(root.right,2*index+2)
            left = traverse(root.left,2*index+1)
            nonlocal maxindex
            maxindex = max(index,maxindex)
            return 1+max(left,right)
        traverse(root,0)
        return maxindex+1 if maxindex!=float('-inf') else 0


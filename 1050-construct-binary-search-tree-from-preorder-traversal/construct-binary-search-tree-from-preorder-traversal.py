# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if preorder==[]:
            return None
        node = TreeNode(preorder[0])
        index = bisect(preorder[1:], node.val)
        node.left = self.bstFromPreorder(preorder[1:index+1])
        node.right = self.bstFromPreorder(preorder[index+1:])
        return node

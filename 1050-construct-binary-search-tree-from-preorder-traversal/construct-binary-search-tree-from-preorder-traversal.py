# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        itr = 0
        n = len(preorder)
        if preorder==[]:
            return None
        def buildTree(lb,rb):
            
            nonlocal itr
            if itr == n:
                return None
            val = preorder[itr]
            if lb>val or rb<val:
                return None
            itr+=1
            node = TreeNode(val)

            node.left = buildTree(lb, val)
            node.right = buildTree(val, rb)
            return node
        return buildTree(float('-inf'),float('inf'))

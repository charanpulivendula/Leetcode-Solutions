# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import deque
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def isleaf(root):
            return not root.left and not root.right
        if isleaf(root):
            return [root.val]
        left = [root.val]
        leaves = []
        right = []
        def findleft(root):
            nonlocal left
            while(root):
                if not isleaf(root):
                    left.append(root.val)
                if root.left:
                    root = root.left
                else:
                    root = root.right

        def findright(root):
            nonlocal right
            while(root):
                if not isleaf(root):
                    right = [root.val]+right
                if root.right:
                    root = root.right
                else:
                    root = root.left
        
        def findleaves(root):
            if not root:
                return
            if isleaf(root):
                leaves.append(root.val)
            
            findleaves(root.left)
            findleaves(root.right)

        if root.left:
            findleft(root.left)
        if root.right:
            findright(root.right)
        findleaves(root)
        return left+leaves+right
        
            
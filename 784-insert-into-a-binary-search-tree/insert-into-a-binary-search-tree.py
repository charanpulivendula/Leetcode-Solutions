# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode((val))
        def bst(root,node):
            if not root:
                return node
            if node.val>=root.val:
                root.right = bst(root.right, node)
            else:
                root.left = bst(root.left, node)
            return root
            
        return bst(root, node)
            

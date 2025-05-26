# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        def build(inorder,preorder):
            if not inorder or not preorder:
                return None
            nodeval = preorder[0]
            node = TreeNode(nodeval)
            index = inorder.index(nodeval)
            node.left = build(inorder[:index], preorder[1:index+1])
            node.right = build(inorder[index+1:],preorder[index+1:])
            return node
        return build(inorder, preorder)
            
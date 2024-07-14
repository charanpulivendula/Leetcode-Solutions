# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # def valueChanger(root):
        #     if not root:
        #         return 0
        #     if not root.left and not root.right:
        #         return root.val
        #     root.val = valueChanger(root.left) or valueChanger(root.right)
        def prune(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            left = prune(root.left)
            right = prune(root.right)
            if left == 0:
                root.left = None
            if right == 0:
                root.right = None
            return root.val or left or right
        prune(root)
        if not root.left and not root.right and not root.val:
            return None
        return root

            

        
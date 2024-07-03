# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def symmetric_check(leftnode,rightnode):
            # print(leftnode.val,rightnode.val)
            if not leftnode and not rightnode:
                return True
            if not leftnode or not rightnode:
                return False
            return leftnode.val == rightnode.val and symmetric_check(leftnode.right,rightnode.left) and symmetric_check(leftnode.left,rightnode.right)
        return symmetric_check(root.left,root.right)
        
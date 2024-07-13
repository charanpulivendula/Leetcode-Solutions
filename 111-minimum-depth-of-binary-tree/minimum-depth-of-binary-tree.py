
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mini = 999999
        if not root.left and not root.right:
            return 1
        if root.left:
            mini = min(mini,1 + self.minDepth(root.left))
        if root.right:
            mini = min(mini,1 + self.minDepth(root.right))
        return mini
        
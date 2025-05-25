# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        stack = [root.val]
        def traverse(root,stack):
            if not root.right and not root.left:
                string = ""
                for elem in stack:
                    string+=str(elem)+"->"
                res.append(string+str(root.val))
            if root.left:
                traverse(root.left,stack+[root.val])
            if root.right:
                traverse(root.right,stack+[root.val])
        traverse(root,[])
        return res

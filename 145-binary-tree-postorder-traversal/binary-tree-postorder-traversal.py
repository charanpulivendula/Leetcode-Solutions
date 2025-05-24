# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s1 = []
        s1.append(root)
        res = []
        while(s1):
            curr = s1.pop()
            res.append(curr.val)
            if curr.left:
                s1.append(curr.left)
            if curr.right:
                s1.append(curr.right)

        return res[::-1]
        
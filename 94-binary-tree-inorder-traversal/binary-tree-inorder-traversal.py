# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root
        while(curr):
            if not curr.left:
                stack.append(curr.val)
                curr = curr.right
            else:
                tail = curr.left
                while(tail.right and tail.right!=curr):
                    tail = tail.right
                if not tail.right:
                    tail.right = curr
                    curr = curr.left
                else:
                    tail.right = None
                    stack.append(curr.val)
                    curr = curr.right
        return stack


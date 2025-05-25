# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([])
        q.append((root,0))
        counter = 1
        res = float('-inf')
        while(q):
            mini = float('inf')
            maxi = float('-inf')
            counter = len(q)
            for _ in range(counter):
                node,val = q.popleft()
                mini = min(mini,val)
                maxi = max(maxi,val)
                if node.left:
                    q.append((node.left,2*val))
                if node.right:
                    q.append((node.right,2*val+1))

            res = max(res,maxi-mini+1)
        return res



        
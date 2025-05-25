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
            _, level_start = q[0]
            _, level_end = q[-1]
            res = max(res, level_end - level_start + 1)
            counter = len(q)
            for _ in range(counter):
                node,val = q.popleft()
                if node.left:
                    q.append((node.left,2*val))
                if node.right:
                    q.append((node.right,2*val+1))

        return res



        
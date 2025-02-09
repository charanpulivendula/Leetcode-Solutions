# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heappush,heappop
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def bst(root):
            if not root:
                return
            heappush(heap,root.val)
            if root.left:
                bst(root.left)
            if root.right:
                bst(root.right)
        bst(root)
        while(k>1 and heap):
            heappop(heap)
            k-=1
        return heappop(heap)

        
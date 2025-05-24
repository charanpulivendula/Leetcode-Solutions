# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)
        def traversal(root,row,col):
            if not root:
                return
            nonlocal hashmap
            hashmap[col].append((row,root.val))
            traversal(root.left,row+1,col-1)
            traversal(root.right,row+1,col+1)
        traversal(root,0,0)
        res = []
        for values in sorted(hashmap.items()):
            temp = []
            for nodes in sorted(values[1]):
                temp.append(nodes[1])
            res.append(temp)
        return res

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
from queue import deque


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        visited = set()

        def traverse(root):
            if not root:
                return
            if root.left:
                parent[root.left] = root
                traverse(root.left)
            if root.right:
                parent[root.right] = root
                traverse(root.right)

        traverse(root)
        q = deque([target])
        visited.add(target)
        while q and k > 0:
            counter = len(q)
            for _ in range(counter):
                node = q.popleft()
                for neighbour in (node.left,node.right,parent.get(node)):
                    if neighbour and neighbour not in visited:
                        visited.add(neighbour)
                        q.append(neighbour)
            # print(q)
            k -= 1

        return[node.val for node in q]

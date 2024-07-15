from collections import deque, defaultdict
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_table = defaultdict(list)
        queue = deque([(root, 0)])  # Pair of node and its column index

        while queue:
            node, column = queue.popleft()

            if node is not None:
                column_table[column].append(node.val)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        # Sort by column index
        sorted_columns = sorted(column_table.keys())
        result = [column_table[col] for col in sorted_columns]

        return result

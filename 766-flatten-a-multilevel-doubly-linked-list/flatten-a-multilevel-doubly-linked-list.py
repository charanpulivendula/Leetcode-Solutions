"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def __init__(self):
        self.prev = None
    def flatten(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if not node:
            return None
        curr = node
        while(curr):
            curnext = curr.next
            if curr.child:
                childhead = self.flatten(curr.child)
                curr.next = childhead
                if childhead:
                    childhead.prev = curr
                childcur = childhead
                while(childcur and childcur.next):
                    childcur=childcur.next
                if childcur:
                    childcur.next = curnext
                if curnext:
                    curnext.prev = childcur
            curr.child = None
            curr = curr.next
        return node


        

            
        
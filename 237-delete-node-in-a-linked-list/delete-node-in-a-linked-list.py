# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        temp = node
        while(temp.next):
            temp.val = temp.next.val
            prev = temp
            temp = temp.next
        prev.next = None

        
        
        
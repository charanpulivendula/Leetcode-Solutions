# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(first,second):
            dummy = ListNode()
            temp = dummy
            while(first and second):
                if first.val>second.val:
                    temp.next = second
                    second = second.next
                else:
                    temp.next = first
                    first = first.next
                temp = temp.next

            if first:
                temp.next = first
            if second:
                temp.next = second
            return dummy.next

        while(len(lists)>1):
            n = len(lists)
            first = lists.pop()
            second = lists.pop()
            merged = merge(first,second)
            lists.append(merged)
        return lists[0] if len(lists)==1 else None
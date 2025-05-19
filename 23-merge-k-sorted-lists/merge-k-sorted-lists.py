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
        n = len(lists)
        interval = 1
        while(interval < n):
            for i in range(0,n - interval,interval*2):
                lists[i] = merge(lists[i],lists[i+interval])
            interval*=2

        return lists[0] if n>0 else None
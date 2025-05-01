class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head or not head.next:
            return head 

        def getKthNode(cur, k):
            while k > 1 and cur:
                cur = cur.next
                k -= 1
            return cur

        def reverse(start):
            prev = None
            curr = start
            while curr:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        temp = head

        while temp:
            kth = getKthNode(temp, k)
            if not kth:
                prev.next = temp
                break
            nextnode = kth.next
            kth.next = None

            new_head = reverse(temp)
            prev.next = new_head
            temp.next = nextnode

            prev = temp
            temp = nextnode

        return dummy.next

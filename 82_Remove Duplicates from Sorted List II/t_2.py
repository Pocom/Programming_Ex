class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        thead = ListNode('a')
        thead.next = head
        pre, cur = None, thead
        while cur:
            pre = cur
            cur = cur.next
            while cur and cur.next and cur.next.val == cur.val:
                t = cur.val
                while cur and cur.val == t:
                    cur = cur.next
                pre.next = cur
        return thead.next

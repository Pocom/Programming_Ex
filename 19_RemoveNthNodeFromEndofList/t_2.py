# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        def reverseListNode(head):
            p, rev = head, None
            while p:
                rev, rev.next, p = p, rev, p.next
            return rev

        rev = reverseListNode(head)
        p = rev
        if n == 1:
            return reverseListNode(p.next)
        else:
            for i in range(n, -1, -1):
                if i == 2:
                    p.next = p.next.next
                    break
                else:
                    p = p.next
            return reverseListNode(rev)

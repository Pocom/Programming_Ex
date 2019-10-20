# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return head

        while head and head.val == val:
            head = head.next
        h1 = h2 = head
        if h1: h2 = h1.next
        while h2:
            if h2.val == val:
                h1.next = h2.next
                h2 = h2.next
            else:
                h1 = h1.next
                h2 = h2.next if h2 else h2
        return head
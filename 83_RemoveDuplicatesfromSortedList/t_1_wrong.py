# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        l1, l2 = head, head.next
        while l2:
            l1.next = l1.next if l1.val == l2.val and l2.next else l2
            l1.next = l2.next if l1.val == l2.val and not l2.next else l1.next
            l2 = l2.next
        return head
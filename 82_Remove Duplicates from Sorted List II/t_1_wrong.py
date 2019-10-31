# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next: return head

        l1 = l2 = head
        value = head.val
        while l1.next:
            l2 = l2.next
            if l2 and l2.val == value:
                while l2.val == value:
                    l2 = l2.next
                if head.val == value:
                    head = l2
                else:
                    l1.next = l2
            elif not l2:
                l1.next = l2
            value = l2.val if l2 else value
        return head

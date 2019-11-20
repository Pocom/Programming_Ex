# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_intersect(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast: return fast
            slow = slow.next
            fast = fast.next.next

        return None

    def detectCycle(self, head):
        if not head:
            return None

        intersect = self.get_intersect(head)

        if not intersect:
            return None

        ptr1 = head
        ptr2 = intersect

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1

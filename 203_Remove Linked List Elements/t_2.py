# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val: head = head.next
        ptr = head
        while ptr and ptr.next:
            while ptr.next and ptr.next.val == val:
                ptr.next = ptr.next.next
            ptr = ptr.next
        return head

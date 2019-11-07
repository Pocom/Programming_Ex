# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next: return head
        head_s = head_l = l1 = l2 = None

        if head.val < x:
            head_s = head
        else:
            head_l = head

        if head_s:
            l1 = head_s
        else:
            l2 = head_l

        head = head.next
        while head:
            if head.val < x:
                if not head_s:
                    head_s = head
                    l1 = head_s
                else:
                    l1.next = head
                    l1 = l1.next
            else:
                if not head_l:
                    head_l = head
                    l2 = head_l
                else:
                    l2.next = head
                    l2 = l2.next

            head = head.next

        if l1:
            l1.next = head_l
        if l2:
            l2.next = None

        return head_s if head_s else head_l

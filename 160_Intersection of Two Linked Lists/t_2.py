# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        ptr1, ptr2 = headA, headB
        while ptr1 != ptr2:
            ptr1 = headB if not ptr1 else ptr1.next
            ptr2 = headA if not ptr2 else ptr2.next
        return ptr1

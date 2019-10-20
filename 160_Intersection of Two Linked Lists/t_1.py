# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dic = {}
        while headA:
            dic[headA] = 0
            headA = headA.next
        while headB:
            if headB in dic:
                return headB
            headB = headB.next
        return None

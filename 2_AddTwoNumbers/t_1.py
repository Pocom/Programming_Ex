# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        re_l = l3
        carry = 0
        while l1 or l2 or carry != 0:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            sum_ = l1.val + l2.val + carry
            if sum_ >= 10:
                l3.val = sum_ % 10
                carry = 1
            else:
                l3.val = sum_
                carry = 0
            l1 = l1.next
            l2 = l2.next
            l3.next = ListNode(0)
            l3 = l3.next
        l3 = re_l if l3.val == 0 else l3
        while l3.next.next:
            l3 = l3.next
        l3.next = None
        return re_l

t = Solution()
ListNode1 = ListNode(5)
ListNode1.next = ListNode(4)
ListNode1.next.next = ListNode(3)
ListNode2 = ListNode(5)
ListNode2.next = ListNode(6)
ListNode2.next.next = ListNode(4)

ListNode3 = t.addTwoNumbers(ListNode1, ListNode2)
while ListNode3:
    print(ListNode3.val)
    ListNode3 = ListNode3.next
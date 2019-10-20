# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        l1, l2 = head, head.next
        while l2:
            if l2.next:
                if l1.val != l2.val:
                    l1.next = l2
                    l1 = l1.next
            else:
                l1.next = l2.next if l1.val == l2.val else l2
            l2 = l2.next
        return head


t = Solution()
l_head = ListNode(1)
l_head.next = ListNode(1)
l_head.next.next = ListNode(1)
l_head.next.next.next = ListNode(1)
l_head.next.next.next.next = ListNode(2)
ret_l_head = t.deleteDuplicates(l_head)

while ret_l_head:
    print(ret_l_head.val)
    ret_l_head = ret_l_head.next
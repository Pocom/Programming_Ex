# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p = head  # 奇头节点
        t = q = p.next  # 偶头节点
        while p and q and q.next:  # 奇、偶头节点以及偶节点的下一节点要存在
            p.next, q.next = q.next, q.next.next
            p, q = p.next, q.next
        p.next = t
        return head

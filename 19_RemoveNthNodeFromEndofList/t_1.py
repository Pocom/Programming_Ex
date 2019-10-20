# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return head  # 为空时返回空
        copy_head = del_node = head  # 初始化
        for i in range(n):
            copy_head = copy_head.next  # 将复制的头节点移动至后续第n个节点
        if not copy_head: head = head.next  # 如果复制的头节点为空，则删除第一个节点
        else:
            while copy_head.next:
                copy_head = copy_head.next
                del_node = del_node.next
            del_node.next = del_node.next.next if n != 1 else None
        return head

# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:

        ptr = head
        while ptr:
            new_node = Node(ptr.val, ptr.next, ptr.random)
            ptr.next = new_node
            ptr = new_node.next

        ptr_old_list, ptr_new_list = head, head.next
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list, ptr_new_list = ptr_old_list.next, ptr_new_list.next
        return head_old


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return head

        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)

            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        ptr_old_list = head  # A->B->C
        ptr_new_list = head.next  # A'->B'->C'
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old

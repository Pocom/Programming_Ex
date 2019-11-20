# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        p = head
        up = []

        while p:
            if p.child:
                if p.next: up.append(p.next)
                p.next, p.child.prev = p.child, p
                p.child = None
            p = p.next
            if p and not p.next and up:
                up_node = up.pop()
                p.next, up_node.prev = up_node, p

        return head

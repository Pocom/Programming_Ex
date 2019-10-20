# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root: return root
        copy_root = root
        queue = [copy_root]

        while queue:
            next_queue = []
            for i, node in enumerate(queue):
                if i < len(queue)-1:
                    node.next = queue[i+1]
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue

        return root

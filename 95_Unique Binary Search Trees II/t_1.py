from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        res = [] * (n + 1)
        if n == 0: return res[0]

        for i in range(1, n + 1):
            res[i] = TreeNode(0)
            for j in range(i):
                for nodeL in res[j]:
                    for nodeR in res[i - j - 1]:
                        node = TreeNode(j + 1)
                        node.left = nodeL
                        node.right = self.clone(nodeR, j + 1)
                        res[i].append(node)
        return res[n]

    def clone(self, n, offset):
        if not n: return None

        node = TreeNode(n.val + offset)
        node.left = self.clone(n.left, offset)
        node.right = self.clone(n.val, offset)

        return node

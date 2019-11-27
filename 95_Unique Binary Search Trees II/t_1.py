# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def generate(start, end):
            if start > end:
                return [None, ]

            all_Trees = []
            for i in range(start, end + 1):
                left = generate(start, i - 1)
                right = generate(i + 1, end)

                for l in left:
                    for r in right:
                        cur_Tree = TreeNode(i)
                        cur_Tree.left = l
                        cur_Tree.right = r
                        all_Trees.append(cur_Tree)

            return all_Trees

        return generate(1, n) if n else []

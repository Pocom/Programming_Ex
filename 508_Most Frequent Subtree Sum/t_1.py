# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:

        def dfs(root, vals):
            if not root: return 0

            cur_val = root.val
            if root.left:
                cur_val += dfs(root.left, vals)
            if root.right:
                cur_val += dfs(root.right, vals)

            if cur_val in vals:
                vals[cur_val] += 1
            else:
                vals[cur_val] = 1

            return cur_val

        if not root: return []
        vals = {}
        dfs(root, vals)

        max_, ret = max(vals.values()), []
        for key in vals.keys():
            if vals[key] == max_:
                ret.append(key)

        return ret

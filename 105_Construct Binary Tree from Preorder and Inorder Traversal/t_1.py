# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        if len(preorder) == 1: return root

        root_pos_of_in = inorder.index(root_val)
        left_vals_in_in = inorder[:root_pos_of_in]
        right_vals_in_in = inorder[root_pos_of_in + 1:]

        left_vals_in_pre = preorder[1:len(left_vals_in_in) + 1]
        right_vals_in_pre = preorder[len(left_vals_in_in) + 1:]

        root.left = self.buildTree(left_vals_in_pre, left_vals_in_in) \
            if left_vals_in_in and left_vals_in_pre else None
        root.right = self.buildTree(right_vals_in_pre, right_vals_in_in) \
            if right_vals_in_in and right_vals_in_pre else None
        return root
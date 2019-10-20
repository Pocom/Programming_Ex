# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ret = True
        if p.val == q.val:
            print("value相等")
            if p.left and q.left:
                print("进入左子树")
                ret = ret and self.isSameTree(p.left, q.left)
            elif not p.left and not q.left:  # 如果在前面加上对于空的判断 这句就是多余的
                print("没有左子树")
                ret = ret and True
            else:
                print("只有一个有左子树")
                return False
            if p.right and q.right:
                print("进入右子树")
                ret = ret and self.isSameTree(p.right, q.right)
            elif not p.right and not q.right:
                print("没有右子树")
                ret = ret and True
            else:
                print("只有一个有右子树")
                return False
        else:
            print("value不相等")
            return False
        return ret


t = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(3)
print(t.isSameTree(t1, t2))

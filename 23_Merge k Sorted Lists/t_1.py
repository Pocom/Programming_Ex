# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :param lists: List[ListNode]
        :return: ListNode
        """

        dic = {}  # 额外空间 O(M)

        for ln in lists:  # 遍历N个链表元素 O(N)
            while ln:
                node = ln
                ln = ln.next
                node.next = None
                if node.val in dic:
                    dic[node.val] += [node]
                else:
                    dic[node.val] = [node]

        if not dic: return None

        keys = sorted(list(dic.keys()))  # M为其中不同数值个数 O(MlogM)
        head = cpy = dic[keys[0]][0]
        dic[keys[0]].pop(0)
        for num in keys:
            for node in dic[num]:
                if node:  # 连接链表 O(1)
                    cpy.next = node
                    cpy = cpy.next
        return head

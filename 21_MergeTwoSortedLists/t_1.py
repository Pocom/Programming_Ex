"""

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


class ListNode:  # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = pre = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 or l2
        return dummy.next


l_1 = ListNode(1)
l_1.next = ListNode(2)
l_1.next.next = ListNode(4)
l_2 = ListNode(1)
l_2.next = ListNode(3)
l_2.next.next = ListNode(4)

t = Solution()

get_1 = ListNode(None)
get_1 = t.mergeTwoLists(l_1, l_2)
while get_1:
    print(get_1.val)
    get_1 = get_1.next


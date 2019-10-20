# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        nums_stack = list()
        while head:
            nums_stack.append(head.val)
            head = head.next
        nums_len = len(nums_stack)
        for pos, num in enumerate(nums_stack[:nums_len//2]):
            if num != nums_stack[-pos-1]:
                return False
        return True

#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        curr = result
        p = val = 0
        while l1 or l2:
            node = ListNode()
            if l1 and l2:
                val = (l1.val + l2.val + p) % 10
                p = floor((l1.val + l2.val + p) / 10)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = (l1.val + p) % 10
                p = floor((l1.val + p) / 10)
                l1 = l1.next
            elif l2:
                val = (l2.val + p) % 10
                p = floor((l2.val + p) / 10)
                l2 = l2.next
            node.val = val
            curr.next = node
            curr = curr.next
        if p > 0:
            node = ListNode()
            node.val = p
            curr.next = node
        return result.next


# @lc code=end

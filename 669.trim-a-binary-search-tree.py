#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        elif root.val < low:
            root = self.trimBST(root.right, low, high)
        elif root.val > high:
            root = self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, root.val - 1)
            root.right = self.trimBST(root.right, root.val + 1, high)
        return root


# @lc code=end

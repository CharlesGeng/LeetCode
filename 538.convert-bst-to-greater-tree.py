#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode, parentVal: int) -> int:
            if root is None:
                return parentVal
            root.val += dfs(root.right, parentVal)
            return dfs(root.left, root.val)

        dfs(root, 0)
        return root


# @lc code=end

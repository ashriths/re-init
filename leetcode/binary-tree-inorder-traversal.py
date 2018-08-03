################################################################################
# Question:
# Binary Tree Inorder Traversal

# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?
################################################################################
# Solution Notes:
# Left, root, right
################################################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret
        if root.left:
            ret.extend(self.inorderTraversal(root.left))
        ret.append(root.val)
        if root.right:
            ret.extend(self.inorderTraversal(root.right))
        return ret
################################################################################
# Question:
# Construct Binary Tree from Preorder and Inorder Traversal

# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7
################################################################################
# Solution Notes:

# Recursive Solution:
# Scrape out the root and then left and right inorder and preorder lists
################################################################################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]
        left_preorder = preorder[1:len(left_inorder)+2]
        right_preorder = preorder[len(left_inorder)+1:]
        # print "Pre", preorder
        # print "In", inorder
        # print 
        # print root_index
        # print "left pre", left_preorder
        # print "Right pre", right_preorder
        # print "Left in", left_inorder
        # print "Right in", right_inorder
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
        
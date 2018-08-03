################################################################################
# Question:
# Binary Tree Zigzag Level Order Traversal

# Given a binary tree, return the zigzag level order traversal of its nodes' values. 
# (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
################################################################################
# Solution Notes:

# Keep two lists/stacks. Insert current level's childred into the next stack 
# based on the level you are on and change next to current when you empty current
################################################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root:
            return ret
        _cur = [(root, 0)]
        _next = []
        to_right = False
        l = 0
        ret = [[]]
        while len(_cur) > 0:
            s, level = _cur.pop()
            if level == l:
                ret[-1].append(s.val)
            else:
                ret.append([s.val])
                l += 1
            if to_right:
                if s.right:
                    _next.append((s.right, level+1))
                if s.left:
                    _next.append((s.left, level+1))
            else:
                if s.left:
                    _next.append((s.left, level+1))
                if s.right:
                    _next.append((s.right, level+1))
            if len(_cur) == 0:
                to_right = not to_right
                _cur = _next
                _next = []
        return ret
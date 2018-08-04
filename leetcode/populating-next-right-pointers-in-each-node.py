################################################################################
# Question:

# Given a binary tree

# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Note:

# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# Example:

# Given the following perfect binary tree,

#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
# After calling your function, the tree should look like:

#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL

################################################################################
# Solution Notes:

# Use Level order traversal. 
################################################################################
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
    
    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str([self.val, self.next.val if self.next else None])

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        _cur = []
        _next = []
        
        if not root:
            return None
        _cur.append(root)
        while len(_cur) > 0:
            for i in range(len(_cur)):
                if i+1 < len(_cur):
                    _n = _cur[i+1]
                else:
                    _n = None
                _cur[i].next = _n
                if _cur[i].left or _cur[i].right:
                    _next.append(_cur[i].left)
                    _next.append(_cur[i].right)
            _cur = _next
            _next = []
        return root



if __name__ == "__main__":
    s = Solution()
    root = TreeLinkNode(0)
    # root.left = TreeLinkNode(1)
    # root.right = TreeLinkNode(2)
    print s.connect(None)             
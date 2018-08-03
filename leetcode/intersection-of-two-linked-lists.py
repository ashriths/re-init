################################################################################
# Question:
# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.


# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
################################################################################
# Solution Notes:

# Two ways
# 1. Get lengths of both lists and forward the longer one by the difference of 
#     lengths then check for equal nodes and return when they are equal.
# 2. Travers both lists till one ends. Attach the head of other list to that 
#     then and wait for equal nodes.
################################################################################
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA = headA
        curB = headB
        while curA and curB and curA != curB:
            curA = curA.next
            curB = curB.next
            
            if not curA and not curB:
                return None
            
            if not curA:
                curA = headB
            if not curB:
                curB = headA
        if curA == curB:
            return curA
        else:
            return None
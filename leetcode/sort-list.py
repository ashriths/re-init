################################################################################
# Question:

# 148. Sort List - Medium


# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

################################################################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def list(self, l):
        s = []
        while l:
            s.append(l.val)
            l = l.next
        return s
        
    def merge(self, h1, h2):
        p = r = ListNode(0)
        while h1 and h2:
            if h1.val < h2.val:
                r.next = h1
                h1 = h1.next
            else:
                r.next = h2
                h2 = h2.next
            r = r.next
        while h2:
            r.next = h2
            h2 = h2.next
            r = r.next
        while h1:
            r.next = h1
            h1 = h1.next
            r = r.next
        #print "After merge", self.list(p.next)
        return p.next    
            
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Split into two lists
        if not head or not head.next:
            return head
        first = head
        first_tail = None
        slow = fast = head
        while fast and fast.next:
            first_tail = slow
            slow = slow.next
            fast = fast.next.next
        
        first_tail.next = None
        #print "Split into ", self.list(first), self.list(slow)
        l1 = self.sortList(first)
        l2 = self.sortList(slow)
        #print "Merging", self.list(l1), self.list(l2)
        return self.merge(l1, l2)

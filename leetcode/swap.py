# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        return str([self.val])

class Solution(object):
    
    def printl(self, head):
        s = []
        while head:
            s.append(head.val)
            head = head.next
        print s
    
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        l = ListNode(0)
        pre = l
        while cur:
            print cur.val
            if cur.next:
                #Even length
                print "Changing ", pre, "->", cur.next 
                pre.next = cur.next
                _next = cur.next.next
                print "Changing ", pre.next, "->", cur 
                pre.next.next = cur
                pre = cur
                cur = _next
            else:
                #Odd Length
                pre.next = cur
                cur = cur.next
            #self.printl(head)
        pre.next = None
        return l.next


if __name__ == '__main__':
    inp = [1,2,3,4]
    head = ListNode(inp[0])
    pre = head
    for i in inp[1:]:
        k = ListNode(i)
        if pre:
            pre.next = k
        pre = k
    s = Solution()
    sw = s.swapPairs(head)
    s.printl(sw)
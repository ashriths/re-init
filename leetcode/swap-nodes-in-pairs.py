# Definition for singly-linked list.
import traceback

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head
        if not a:
            return a
        _head = a.next if a.next else a
        # print _head.val
        # print a.next.val
        # print a.next.next.next.val
        b = a.next if a else None
        while a and b:
            try:
                b = a.next
                c = b.next
                d = c.next if c else None
                a.next = d if d else c
                b.next = a
                a = c
                b = d
            except:
                print a.val, b.val
                traceback.print_exc()
                raise
        return _head

if __name__ == "__main__":
    inp = [1]
    head = ListNode(inp[0])
    pre = head
    for i in inp[1:]:
        k = ListNode(i)
        if pre:
            pre.next = k
        pre = k
    s = Solution()
    print s.swapPairs(head)





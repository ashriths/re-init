# Copy List with Random Pointer

# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# Solution Notes:

# 1. O(n) extra space solution
#       Create a map of original node to next
#       Create a copy of original with just next nodes
#       Make the next of original point to the corresponding new node in copy.abs
#       Make the random of the new copy point to the original node such that
#       copy.random = copy.random.random.next
#       Fix the next of original from the orignal map created in step 2


# 2. O(1) space solution
#       Insert the copy of each node next to the original node in the same Linkedlist
#       new.random = cur.random.next


class Solution(object):
    
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        return self.copyRandomListO1(head)
    
    def print_list(self, head):
        r = []
        while head:
            r.append([head.label, head.random.label if head.random else None, id(head)]) 
            head = head.next
        print r
    
    def copyRandomListOn(self, head):
        original_map = {}
        cur = head
        copy_head = copy = RandomListNode(0)
        while cur:
            original_map[cur] = cur.next
            copy.next = RandomListNode(cur.label)
            copy = copy.next
            copy.random = cur
            pre_o = cur
            cur = cur.next
            pre_o.next = copy
        copy_head = copy_head.next
        copy = copy_head
        while copy:
            copy.random = copy.random.random.next if copy.random.random else None
            copy = copy.next
        cur = head
        while cur:
            cur.next = original_map[cur]
            cur = cur.next

        # self.print_list(head)
        # self.print_list(copy_head)
        return None

    def copyRandomListO1(self, head):
        cur = head
        while cur:
            new = RandomListNode(cur.label)
            new.next = cur.next
            cur.next = new
            cur = new.next
        cur = head
        while cur:
            new = cur.next
            new.random = cur.random.next if cur.random else None
            cur = new.next
        cur = head
        copy_head = cur.next
        while cur:
            new = cur.next
            cur.next = new.next
            new.next = new.next.next if new.next else None
            cur = cur.next 

        # self.print_list(head)
        # self.print_list(copy_head)
        return copy_head

def make_ll(l):
    head = RandomListNode(0)
    cur = head
    _list = []
    for i in l:
        cur.next = RandomListNode(i)
        _list.append(cur.next)
        cur = cur.next
    return head.next, _list

if __name__ == "__main__":
    
    m = {
        0: 2,
        1: 0,
        2: 4,
        3: 2,
        4: 1
    }
    head, nodes = make_ll([0,1,2,3,4])
    for node in nodes:
        node.random = nodes[m[node.label]]
    s = Solution()
    s.print_list(head)
    print
    s.copyRandomList(head)
    

        
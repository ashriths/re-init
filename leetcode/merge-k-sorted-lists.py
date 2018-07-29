################################################################################
# Question:

# Merge k sorted linked lists and return it as one sorted list. 
# Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
################################################################################
# Solution Notes:

# Time complexity: O(kn)
# Can do better using a priority queue with O(nlogk)

# Just normal merge sort's merge technique.
################################################################################
# Definition for singly-linked list.
import json


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        root = ListNode(0)
        res = root
        try:
            cur = lists[0]
        except:
            return []
        iteration = 0
        while len(lists) > 0:
            #print "*" * 10, iteration, "*" * 10
            iteration += 1
            all_none = True
            cur = lists[0]
            arg = 0
            empty = []
            for i, l in enumerate(lists):
                if l == None:
                    empty.append(i)
                    break
                if l.val < cur.val:
                    #print "Changing min ", cur.val, "->", l.val
                    cur = l
                    arg = i
            if empty:
                lists.pop(empty[0])
                continue
            if cur == None:
                continue
            res.next = ListNode(cur.val)
            res = res.next
            #print "Adding ", cur.val
            if lists[arg].next == None:
                #print "Done with list", arg
                lists.pop(arg)
            else:
                #print "Changing head of ", arg, "->", lists[arg].next.val
                lists[arg] = lists[arg].next
        return root.next


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def stringToListNodeArray(input):
    listNodeArrays = json.loads(input)
    nodes = []
    for listNodeArray in listNodeArrays:
        nodes.append(stringToListNode(json.dumps(listNodeArray)))
    return nodes


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    #lines = readlines()
    lines = iter([
        '[[],[],[3,2,1]]'
    ])
    while True:
        try:
            line = lines.next()
            lists = stringToListNodeArray(line)

            ret = Solution().mergeKLists(lists)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
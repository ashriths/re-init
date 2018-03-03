
a = [1,2,3,2]
k = 5

from collections import deque

def  maxLength(a, k):
    q = deque()
    m = 0
    s = 0
    for i in a:
        q.append(i)
        s += i
        if s <= k:
            m = max(m, len(q))
        else:
            s -= q.popleft()
    return m

print maxLength(a, k)
from string import ascii_lowercase

def evenSubarray(ar, k):
    r = []
    if not ar:
        return r
    for size in range(1,len(ar)+1):
        #print "Size", size
        left = 0
        right = 1
        odd = []
        if ar[left] % 2:
            odd.append(ar[left])
        while right < len(ar):
            #print ar[right]
            #print "left", left, "right", right
            #print odd, ar[left:right]
            if len(odd) <= k and right - left == size:
                if ar[left:right]:
                    r.append(ar[left:right])
                    #print ar[left:right]
            if ar[right] % 2 != 0:
                odd.append(ar[right])
            
            right += 1
            if right - left > size:
                if left >=0 and ar[left] % 2:
                    odd.remove(ar[left])
                left += 1
        
        if len(odd) <= k:
                if ar[left:right]:
                    r.append(ar[left:right])
                    #print ar[left:right]
        #print odd, ar[left:right]
    return len(r)      

def evenSubarrayCount(ar, k):
    count = 0
    p = [0] * len(ar)
    odd = 0
    for i in xrange(len(ar)):
        p[odd] += 1
        
        if ar[i] % 2:
            odd += 1
        if odd >= k:
            count += p[odd - k]
    return count


def subseq(s):
    if len(s) == 1:
        return [s]
    for i in range(len(s)):
        start = 0
        return subseq(s[0:i]) + subseq([i+1:])

def subArray(arr, n): 
    r = []
    # Pick starting point 
    for i in range(0,n): 
  
        # Pick ending point 
        for j in range(i,n): 
  
            # Print subarray between 
            # current starting 
            # and ending points 
            s = ""
            for k in range(i,j+1): 
                s += arr[k]
  
            r.append(s)


if __name__ == "__main__":
    #print evenSubarray([6,3,5,8], 1)
    #print evenSubarrayCount([6,3,5,8], 1)
    print subArray("ab")
#abcdefghijklmnopqrstuvwxyz
#01111001111111111011111111
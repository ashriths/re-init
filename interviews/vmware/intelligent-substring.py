from string import ascii_lowercase

def getSpecialSubstring(s, k, charValue):
    normal = set()
    for l,bit in zip(ascii_lowercase, charValue):
        if bit == "0":
            normal.add(l)
    #print "normal ->", normal
    maxLen = 0
    left = 0
    right = 0
    seenNormal = []
    while right < len(s):
        cur = s[right]
        # if the number of normal has not reached k then expand on right
        if len(seenNormal) < k:
            if cur in normal:
                seenNormal.append(cur)
            right += 1
        elif len(seenNormal) == k:
            if cur in normal:
                # Shrink from left side till the max number of normal is less than k
                #print "Shrinking left for ", cur 
                seenNormal.append(cur)
                while len(seenNormal) > k:
                    #print "S[left]", s[left]
                    if s[left] in normal:
                        #print "removing", s[left]
                        seenNormal.remove(s[left])
                    left += 1
            right += 1
        print s[left:right], seenNormal
        maxLen = max(maxLen, right - left)
    return maxLen

if __name__ == "__main__":
    print getSpecialSubstring("giraffe", 2, "01111001111111111011111111")
    
#abcdefghijklmnopqrstuvwxyz
#01111001111111111011111111
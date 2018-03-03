if __name__== "__main__":
    a = [10,9,8,7,6,5,4,1,3,2]
    i, j, k = 0,1,2

    while i < j and j < k and k < len(a):
        if  a[i] < a[j] and a[i] < a[k] and a[j] > a[k]:
            break

        i += 1


class RangeSumService:
    # [0, 2, 3, 4]
    def __init__(self, a):
        # Preprocessing.
        # self.state = ...
        self.lookup = []
        k = 0
        for key,i in enumerate(a):
            k += i
            self.lookup.append(k)
    
    def handle_request(self, i, j):
        r = self.lookup[j]
        if i > 0:
            r -= self.lookup[i-1]
        return r


a = [[0, 2, 3, 4], #i 9
     [1, -5, 2, 3], # 1
     [-2, 3, 4, 5], 
     [-10, 2, 3, 1]] # -4

    
class AreaSumService:
    def __init__(self, a):
        # Preprocessing.
        # self.state = ...
        self.lookup = []
        m = len(a)
        n = len(a[0])
        g = 0
        for i in range(m):
            self.lookup.append([])
            for j in range(n):
                g = 0
                for k in range(0,j+1):
                    g += a[i][k]
                if i > 0:
                    g += self.lookup[i-1][j]
                #print i, j, a[i][j], g
                self.lookup[i].append(g)
                
    
    def handle_request(self, i1, j1, i2, j2):
        return self.lookup[i2][j2] - self.lookup[i2][j1] - self.lookup[i1][j2] + self.lookup[i1][j1]
    
    def print_lookup(self):
        for i in self.lookup:
            for j in i:
                print j,
            print

s = AreaSumService(a)
#print s.print_lookup()
print s.handle_request(1,1,2,2)

#s = RangeSumService([10, 2, 3, 4])
#print s.lookup
#print s.handle_request(1, 2)

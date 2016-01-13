class Solution(object):
    res = [0]
    def numSquares(self, n):
        while len(self.res) <=n:
            self.res += [min([self.res[-i*i] for i in range(1,int(len(self.res)**0.5)+1)]) +1]     
        return self.res[n]

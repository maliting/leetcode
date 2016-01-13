class Solution(object):
    def isHappy(self,n):
        s={n:1}
        while n!=1:
            n=sum([int(i)**2 for i in str(n)])        
            if n not in s : 
                s[n]=1
            else:
                return False
        return True

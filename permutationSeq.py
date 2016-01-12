class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def f(x):
            c=1
            for i in range(1,x+1):
                c=c*i
            return c
        a=[str(i) for i in range(1,n+1)]
        r=''
        while n-1>=0:
            sh,k=k/f(n-1),k%f(n-1)
            if k>0 :
                r +=a[sh]
                del a[sh]
            else :
                r +=a[sh-1]
                del a[sh-1]
            n-=1
        
        return r

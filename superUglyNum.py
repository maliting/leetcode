class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglyNum=[1]
        k=len(primes)
        length=1
        Tindex=[0]*k
        while length<n :
            T=[uglyNum[Tindex[i]]*primes[i] for i in range(k)]
            a=min(T)
 #           for i in range(k):
 #               if a==T[i] :Tindex[i] +=1
            Tindex=[a==T[i] and Tindex[i]+1 or Tindex[i] for i in range(k)]
            uglyNum.append(a)
            length +=1
        return uglyNum[-1]

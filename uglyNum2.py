class Solution(object):
    def nthUglyNumber(self, n):
        uglyNum=[1]
        Tindex2=0;Tindex3=0;Tindex5=0
        length=1
        while length<n:
             T2=uglyNum[Tindex2]*2
             T3=uglyNum[Tindex3]*3
             T5=uglyNum[Tindex5]*5
             a=min([T2,T3,T5])
             uglyNum.append(a)
             if a==T2 : Tindex2 +=1
             if a==T3 : Tindex3 +=1
             if a==T5 : Tindex5 +=1
             length +=1
        return uglyNum[-1]

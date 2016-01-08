class Solution(object):
    def addDigits(self,num):
        if num>=0 and num <=9 : return num
        else:
            l=list(str(num))
            s=[int(x) for x in l]
            s=sum(s)
            return self.addDigits(s)

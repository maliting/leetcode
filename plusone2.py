
def plusone(digits):
	n=len(digits)
	s=0
	for i in range(n):
		c=digits[i]*10**(n-1-i)
		s=s+c
	s=s+1	
	l=[]
	while(s>=10):		
		l.append(s%10)
		s=s/10
	l.append(s)
	l.reverse()
	return l
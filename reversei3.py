def reverse(x):
	if x==0: return 0
	if x>0:
		n=len(str(x))
		y=0;i=0
		while x>=10:
			c=x%10
			y=y+c*10**(n-1-i)
			i+=1
			x=x/10
		y=y+x
		if(y>2147483647): return 0
    	else: return y
	if x<0:
		x=-x
		n=len(str(x))
		y=0;i=0
		while x>=10:
			c=x%10
			y=y+c*10**(n-1-i)
			i+=1
			x=x/10
		y=y+x
		y=-y
		if(y<-2147483647): return 0
    	else: return y
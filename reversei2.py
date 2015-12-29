def reversei(x):
	if x>=0:
		r=int(str(x)[::-1])
		if r>2147483647:
			return 0
		else:
			return r
	else:
		r=-1*int(str(-1*x)[::-1])
		if r<-2147483647:
			return 0
		else:
			return r
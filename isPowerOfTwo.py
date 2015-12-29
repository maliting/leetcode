def isPowerOfTwo(n):
	if n<=0:return False
	elif n==1:return True
	else:
		if n%2==1: return False
		else: return isPowerOfTwo(n/2)
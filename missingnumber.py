
def missingnumber(nums):
	n=len(nums)
	asum=n*(n+1)/2
	bsum=sum(nums)
	return asum-bsum
def threeSum(nums):
	nums.sort()
	L=[]
	if (len(nums)<2 or nums[0]>0 or nums[-1]<0):return L	
	else:
		while len(nums)>=3:
			for i in range(len(nums)-2):
				for k in range(i+1,len(nums)-1):
					for j in range(i+2,len(nums)):
						if -(nums[i]+nums[k])==nums[j] and nums[i]<=nums[k]<=nums[j]:
							li=(nums[i],nums[k],nums[j])
							L.append(li)							
			del nums[i]				
		L=list(set(tuple(L)))
		result=[]
		for i in range(len(L)):
			result.append(list(L[i]))
		return result
		
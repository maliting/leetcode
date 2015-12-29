def threeSum(nums):
	s1=[i for i in nums if nums.count(i)==1]
	s2=[i for i in nums if nums.count(i)>=2]
	s0=nums.count(0)	
	s3=(list(set(s2)))*2
	s1.extend(s3)
	if s0>=3:s1.append(0)
	nums=s1
	nums.sort()
	L=[]
	if (len(nums)<2 or nums[0]>0 or nums[-1]<0):return L	
	else:
		while len(nums)>=3:	
			ix=len(nums)-1
			for k in range(1,len(nums)-1):				
				for j in range(ix,k,-1):
					if -(nums[0]+nums[k])==nums[j]:
						li=[nums[0],nums[k],nums[j]]
						if li in L :continue
						L.append(li)
						ix=j-1
						break				
			del nums[0]				
		#L=list(set(tuple(L)))
		#result=[]
		#for i in range(len(L)):
		#	result.append(list(L[i]))
		return L
def hIndex(citations):
	citations.sort()
	if len(citations)==0:return 0
	maxc=citations[-1]
	for i in range(maxc,-1,-1):
		count=0
		for j in range(len(citations)):
			if citations[j]>=i: count+=1
		if count>=i: return i
		
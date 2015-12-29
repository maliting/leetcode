from numpy import *
import string

#class Solution(object):
def reverse(x):
	if x==0:return 0
	y='%d' %x
	y=list(y)
	if x>0:	
		y.reverse()
		for i in range(len(y)):
			while(y[0]=='0'):
				del(y[0])				
		z=''
		z=z.join(y)
		iz=string.atoi(z)
		if iz>2147483647:return 0
		else: return iz
	else:
		del(y[0])
		y.reverse()		
		for i in range(len(y)):
			while(y[0]=='0'):
				del(y[0])					
		z=''
		z=z.join(y)
		iz=string.atoi(z)		
		if iz>2147483647:return 0
		else: return -iz			
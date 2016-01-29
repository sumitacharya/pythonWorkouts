#!/usr/bin/python
# Aa small module that can be used in other programs

# Coverts upper case to lower case
def upper2Lower(upper):
	if ord(upper)>64 and ord(upper)<91:
		return chr(ord(upper)+32)
	else :
		return upper

# Converts lower case to upper case
def lower2Upper(lower):
	if ord(lower)>=97 and ord(lower)<=122:
		return chr(ord(lower)-32)
	else :
		return lower
	

# test cases
#print upper2Lower('A')
#print upper2Lower('z')

#print"\n\n", lower2Upper('s')  
#print lower2Upper('K')


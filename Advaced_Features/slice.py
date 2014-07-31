L = ['Micheal', 'Hanson', 'William', 'Lucy', 'Frank'] 
# if you want to get the first three values in a list
# 1> The simplest way
def getFirstThreeValueOfList1(L):
	subL1 = [L[0], L[1], L[2]]
	return subL1

# 2> Use a loop
def getSubList(L = None,  n = 3):
	if (not isinstance(L, (list)) and not isinstance(n, (int, float))):
		 raise TypeError('bad operand type')
	subL2 = []
	for i in range(n):
		subL2.append[L[i]] 
	return subL2

# 3> Use Slice feature
def getSubListBySlice(L, first = 0, last = -1):
	if (not isinstance(L, (list)) and not isinstance((first, last), (int, float))):
		raise TypeError('bad operand type')
	if last > 0 and last > first:
		return L[first:last]
	elif last < 0 and last + len(L) > first:
		return L[first:last]
	else: 
		raise TypeError('Argument value error')

# 

# Test
print L
print getSubListBySlice(L, 0, 2)
print getSubListBySlice(L, 3)
print getSubListBySlice(L, -3)
print getSubListBySlice(L, 20, 30)


####If there is a list and you want to get a value every 3 values behind
def getValuePerXValue(L, n):
	return L[::n]

# Test
NumList = range(100)
print getValuePerXValue(NumList, 22)


####  Iterator  ####
from collections import Iterable
print isinstance('ABC', Iterable)
print isinstance([], Iterable)
print isinstance(123, Iterable)

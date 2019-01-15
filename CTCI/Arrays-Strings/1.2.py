#1.2 Given two strings, write a method to decide if one is a permutation of the other

#Solution 1: Create a dictionary, increment for chars in s1
#Decrement for chars in s2. If negative entry, return False

def isPermutation(s1, s2):
	seen = {}
	if len(s1) != len(s2):
		return False
	for c in s1:
		if c in seen:
			seen[c] += 1
		else:
			seen[c] = 1
	for c in s2:
		if c not in seen:
			return False 
		if c in seen:
			if seen[c] == 0:
				return False
			else:
				seen[c] -= 1
	return True

print(isPermutation('race', 'rack'))
print(isPermutation('abcdef', 'fedcba'))
print(isPermutation('racecar', 'racecar'))


#Solution 2: Sort strings and check concurrent values
'''
def isPermutation(s1, s2):
	if len(s1) != len(s2):
		return False
	s1 = list(s1)
	s2 = list(s2)
	length = len(s1)
	quick_sort(s1, 0, len(s1)-1)
	quick_sort(s2, 0, len(s2)-1)
	for i in range(0, length):
		if s1[i] != s2[i]:
			return False
	return True


def quick_sort(arr, low, high):
    if low < high:
    	pi = partition(arr, low, high)
    	quick_sort(arr, low, pi-1)
    	quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
    	if arr[j] <= pivot:
    		i = i + 1
    		arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

print(isPermutation('race', 'rack'))
print(isPermutation('abcdef', 'fedcba'))
print(isPermutation('racecar', 'racecar'))
'''
#1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
#What if you cannot use additional data structures
'''
Solution 1: quicksort the array and make sure no two concurrent elements are the same

def isUnique(s):
	length = len(s)
	s = list(s)
	if len(s) > 128:
		return False
	quick_sort(s, 0, length-1)
	for i in range(0, length-1):
		if s[i] == s[i+1]:
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

s='abcdefghijklmnopqrstuvwxyzz'
print(isUnique(s))
s='abcdefghijklmnopqrstuvwxyz'
print(isUnique(s))
s='asdadgregegwefwefewf'
print(isUnique(s))
'''
#Solution 2: Create a dictionary making checking each elt to values in the dictionary
#if there are no collisions, return True

def isUnique(s):
	seen = {}
	for c in s:
		if c in seen:
			return False
		else:
			seen[c] = 1
	return True

s='abcdefghijklmnopqrstuvwxyzz'
print(isUnique(s))
s='abcdefghijklmnopqrstuvwxyz'
print(isUnique(s))
s='asdadgregegwefwefewf'
print(isUnique(s))














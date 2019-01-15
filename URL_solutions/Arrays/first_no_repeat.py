#Q First non-repeating integers in an array

def first_no_repeat(arr):
	if not arr:
		return None
	if len(arr) == 1:
		return arr[0]
	seen = {}
	for elt in arr:
		if elt not in seen:
			seen[elt] = 1
		else:
			seen[elt] += 1
	for elt in arr:
		if seen[elt] == 1:
			return elt

li = [1,1,1,1,1,1,1,1,1,2,3,3,3,3,3,4,5,6,7,9]
print(first_no_repeat(li))
li = []
print(first_no_repeat(li))
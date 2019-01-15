#Q: Find the second minimum element of an array

def second_min(arr):
	if len(arr) < 2:
		return None
	#if elts must be distinct add:
	#arr = set(arr)
	#arr = list(arr)
	mi = arr[0]
	target = 0
	for i in range(1, len(arr)):
		if arr[i] < mi:
			mi = arr
			target = i
	del arr[target]
	#OR
	# del min(arr)
	return min(arr)

li = [4,6,7,11,43,72,21,25,32,73,9]
print(second_min(li))
li = []
print(second_min(li))


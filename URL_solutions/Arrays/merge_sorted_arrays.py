def merge_sorted_arrays(arr1, arr2):
	if not arr1 and not arr2:
		return None
	if not arr1:
		return arr2
	if not arr2:
		return arr1
	res = []
	arr1 = arr1[::-1]
	arr2 = arr2[::-1]

	while arr1 and arr2:
		if arr1[-1] < arr2[-1]:
			res.append(arr1[-1])
			arr1.pop()
		else:
			res.append(arr2[-1])
			arr2.pop()
	print('Passed first phase')
	if arr1:
		while arr1:
			res.append(arr1[-1])
			arr1.pop()
	else:
		while arr2:
			res.append(arr2[-1])
			arr2.pop()
	return res

li1 = [1,2,3,4,4,4,5,6,7,8,9]
li2 = [1,2,2,2,3,7,8,8,8,9,11,12,13]
print(merge_sorted_arrays(li1, li2))

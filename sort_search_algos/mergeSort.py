def mergeSort(arr):
	length = len(arr)
	#decompose until arrays are length of 1
	if length > 1:
		mid = length//2
		#create two temp arrays each of which are
		#half of the array
		L = arr[:mid]
		R = arr[mid:]
		#continue to decompose the halves
		mergeSort(L)
		mergeSort(R)

		i = j = k = 0
		#precalculate lengths for efficiency
		lengthL = len(L)
		lengthR = len(R)
		#until all of one array has been sorted
		while i < lengthL and j < lengthR:
			#if the data in the left set is smaller, insert it
			if L[i] < R[j]:
				arr[k] = L[i]
				i+=1
			else:
				#if the data in the right set is smaller, insert it
				arr[k] = R[j]
				j+=1
			#increment the index of the temp final returned array
			k+=1
		#At this point insert the remaining data from one of the arrays
		#Only one will have values that have not been sorted
		while i < lengthL: 
			arr[k] = L[i]
			i+=1
			k+=1
		while j < lengthR:
			arr[k] = R[j]
			j+=1
			k+=1
arr = [12, 11, 13, 5, 6, 7]  
mergeSort(arr)  
print(arr) 
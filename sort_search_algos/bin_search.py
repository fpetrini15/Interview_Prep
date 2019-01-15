def bin_search(arr, low, high, target):
	#so long as the low index remains less than the high index
	if low <= high:
		#compute the middle value
		mid = ((high+1)+low)//2
		#return the index if the value is found
		if arr[mid] == target:
			return mid
		#if the value is > than target, ignore the lower
		#half of the array and repeat process with upper half
		if arr[mid] > target:
			return bin_search(arr, low, mid-1, target)
		#if the value is < than target, ignore the upper
		#half of the array and repeat process with lower half
		else:
			return	bin_search(arr, mid+1, high, target)
	#if not found, return -1
	return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8] 
n = len(arr) 
index = bin_search(arr,0,n-1, 10)
print(index)
print(arr[index])
  
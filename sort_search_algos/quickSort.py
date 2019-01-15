def quick_sort(arr, low, high):
    #if the low index is greater than the high
    #index, the sorting is complete
    if low < high:
        #get the first pivot into place (sorted)
        pi = partition(arr, low, high)
        #sort everything to the left of the original pivot
        quick_sort(arr, low, pi-1)
        #sort everything to the right of the original pivot
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    i = low-1
    #set pivot to last element
    pivot = arr[high]
    #go through all the elts from low to pivot-1
    for j in range(low, high):
        #if elt is <= pivot, increment i and swap
        #this value with that at index i
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j], arr[i]
    #at the end, swap the last element with the elt 
    #at index i+1
    arr[i+1],arr[high] = arr[high], arr[i+1]
    return(i+1)



arr = [2, 6, 5, 0, 8, 7, 1, 3] 
n = len(arr) 
quick_sort(arr,0,n-1) 
  
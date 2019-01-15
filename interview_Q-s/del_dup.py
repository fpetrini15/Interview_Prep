def del_dup(nums, val):
	nums = [i for i in nums if i != val]
	print(nums)

nums = [3,2,2,3]
del_dup(nums, 3)
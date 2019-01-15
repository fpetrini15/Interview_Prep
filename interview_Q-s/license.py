def convert(nums):
	solutions = []
	parameters = {}
	for i in range(0, len(nums)-1):
		for j in range(i+1, len(nums)):
			val = nums[i] + nums[j]
			c = 0 - val
			if c in nums and nums.index(c) != i and nums.index(c) != j:
				temp = [nums[i], nums[j], nums[nums.index(c)]]
				temp.sort()
				if i == 0 and j == 11:
					import pdb; pdb.set_trace()
				if (temp[0], temp[1], temp[2]) in parameters:
					continue
				else:
					parameters[temp[0], temp[1], temp[2]] = 1
					solutions.append([temp[0], temp[1], temp[2]])
	return solutions

nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
convert(nums)

'''
"a-a-a-a-"
"AAAA"
1
length = 4
remainder = 0
want to insert at 1,3,5

"2-5g-3-J"
2
length = 5
remainder = 1
want to insert at 1, 4

"5F3Z-2e-9-w"
4
length = 8
remainder = 0
want to insert at 4 --> remainder + K

'''

def all_numeric_combos(digits):
	if digits == "":
		return []
	nums = { '2': ['a','b','c'],
		'3': ['d','e','f'],
		'4': ['g','h','i'],
		'5': ['j','k','l'],
		'6': ['m','n','o'],
		'7': ['p','q','r','s'],
		'8': ['t','u','v'],
		'9': ['w','x','y','z']}
	res = ['']
	import pdb; pdb.set_trace()
	for digit in digits:
		res = [i+j for i in res for j in nums[digit]]
	return res

digits = '223'
all_numeric_combos(digits)
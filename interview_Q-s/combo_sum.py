def combo_sum(candidates, target):

	candidates.sort()
	res = []
	#import pdb; pdb.set_trace()
	for i, c in enumerate(candidates):
		if c<target:
			for sub in combo_sum(candidates[i:], target-c):
				res.append([c] + sub)
		elif c > target:
			break 
		elif c==target:
			res.append([c])
	return res

candidates = [2,3,6,7]
target = 7
print(combo_sum(candidates, target))

'''
2, 7 --> [2] + sub
2, 5 --> [2], [3]
2, 3 --> 
2, 1

[2,2,3]
[7]

2, 2, 2 --> 1
'''
from collections import deque

def reverse_k_elts(d, k):
	temp = deque()
	for i in range(0,k):
		val = d.popleft()
		temp.append(val)
	while temp:
		val = temp.pop()
		d.append(val)
	stop = len(d) - k
	for i in range(0, stop):
		val = d.popleft()
		d.append(val)
	return d







d = deque()
for i in range(0,7):
	d.append(i)

#0,1,2,3,4,5,6

reverse_k_elts(d, 4)
for each in d:
	print(each)
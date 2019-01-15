#Input: [1,2,50,52,75]
def find_gap(li):
	missing = ''
	if li[0] != 0:
		if li[0] == 1:
			missing = missing + '0,'
		else:
			end = li[0] - 1
			missing = missing + '0-' + str(end)
	length = len(li)-1
	for index in range(0, length):
		if li[index] + 1 != li[index + 1]:
			if li[index] + 2 == li[index+1]:
				end = li[index+1]-1
				missing = missing + str(end) + ','
			else:
				start = li[index]+1
				end = li[index+1]-1
				missing = missing + str(start) + '-' + str(end) + ','
	start = li[index+1] + 1
	end = 99
	if start == end:
		missing = missing + '99'
	else:
		missing = missing + str(start) + '-' + str(end)
	return missing

li = [0,1,2,33,50,52,75,98]
print(find_gap(li))

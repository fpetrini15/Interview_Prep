#1.3: Write a method to replace all the spaces in a string with '%20'

def URLify(s):
	s = list(s)
	start = 0
	for index in range(len(s)-1, -1, -1):
		if s[index] != " ":
			start = 1
		elif s[index] == " " and start == 0:
			del s[index]
		elif s[index] == " " and start == 1:
			s[index] = '%20'
	s = "".join(s)
	return s

s = 'Mr John Smith    '
print(URLify(s))

#Time Complexity: O(n)
#Space Complexity O(1)
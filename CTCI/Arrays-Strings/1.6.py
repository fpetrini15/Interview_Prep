#1.6 Implement a method to perform basic string compression using the
#counts of repeated characters. For example, the string 'aabcccccaaa'
#would be a2b1c5a3. If the 'compressed' string would not become smaller
#than the original string, you method should return the original string.
#Assumed only upper and lowercase letters.

def string_compress(string):
	letter = ''
	compressed = ''
	start = 0
	count = 0
	for c in string:
		if start == 0:
			letter = c
			start = 1
			count = 1
		elif c != letter:
			compressed = compressed + letter + str(count)
			letter = c
			count = 1
		else:
			count += 1
	compressed = compressed + letter + str(count)
	if len(string) < len(compressed):
		return string
	return compressed

string = 'aabcccccaaa'
print(string_compress(string))
string = 'abc'
print(string_compress(string))


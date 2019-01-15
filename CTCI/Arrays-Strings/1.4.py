#1.4 Given a string, write a function to check if it is a permutation of a palindrome. 

def potentialPalindrome(s):
	seen = {}
	for c in s:
		if c in seen:
			seen[c] += 1
		else:
			seen[c] = 1
	odd = 0
	if " " in seen:
		del seen[" "]
	for elt in seen:
		if seen[elt] % 2 == 1:
			odd += 1
		if odd > 1:
			return False
	return True

print(potentialPalindrome('taco cat'))
print(potentialPalindrome('racecar'))
print(potentialPalindrome('hello world'))
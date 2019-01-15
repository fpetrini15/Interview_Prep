#1.5 There are three types of edits that can be performed on strings: insert a character,
#remove a character, or replace a character. Given two strings, write a function to check
#if they are one edit (or zero edits) away.

def wasEdited(s1, s2):
	seen = {}
	if abs(len(s1) - len(s2)) > 1:
		return False
	for c in s1:
		if c in seen:
			seen[c] += 1
		else:
			seen[c] = 1
	strike = 0
	for c in s2:
		if c not in seen:
			strike += 1
		if strike > 1:
			return False
	return True

print(wasEdited('pale', 'ple'))
print(wasEdited('pales', 'pale'))
print(wasEdited('pale', 'bale'))
print(wasEdited('pale', 'bake'))

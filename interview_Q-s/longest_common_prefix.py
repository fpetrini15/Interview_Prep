def lcp(strs):

	if not strs:
		return ""
	s1 = min(strs)
	s2 = max(strs)
	import pdb; pdb.set_trace()
	for index, c in enumerate(s1):
		if elt != s2[index]:
			return s1[:index]
	return s1

li = ["flower","flow","flight"]
print(lcp(li))
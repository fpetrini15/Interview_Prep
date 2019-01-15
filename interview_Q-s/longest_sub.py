def lengthOfLongestSubstring(s):
    sequence = {}
    count = 0
    maximum = 0
    for c in s:
        if c not in sequence:
            count += 1
            sequence[c] = 1
        else:
            sequence.clear()
            count = 1
            sequence[c] = 1
        if count > maximum:
                maximum = count
    print(maximum)
    return maximum

s = "''''"
lengthOfLongestSubstring(s)
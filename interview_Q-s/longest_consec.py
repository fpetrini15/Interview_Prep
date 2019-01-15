def longest_consec(nums):
    nums = set(nums)
    counter = 1
    res = 0
    if len(nums) < 1:
        return 0
    while nums:
        import pdb; pdb.set_trace()
        cursor = nums.pop()
        i = cursor
        bool1, bool2 = True, True
        while bool1:
            if i + 1 in nums:
                i = i+1
                counter += 1
            else:
                bool1 = False
        i = cursor
        while bool2:
            if i - 1 in nums:
                i = i-1
                counter += 1
            else:
                bool2 = False
        res = max(res, counter)
        counter = 1 
    return res

nums = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
print(longest_consec(nums))
        
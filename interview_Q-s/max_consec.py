def max_consec(nums):
    if len(nums) == 0:
        return 0
    counter = 0
    maximum = 0
    length = len(nums)-1
    for index, elt in enumerate(nums):
        if elt == 1:
            while index <= length and nums[index] == 1:
                counter += 1
                index += 1
            if counter > maximum:
                maximum = counter
            counter = 0
    print(maximum)
    return maximum

nums = [1,1,0,1,1,1]
max_consec(nums)

def removeDuplicates(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i != j:
                nums[i] = " "

    temp_lst = []
    for i in nums:
        if str(i) != " ":
            temp_lst.append(i)

    nums = temp_lst
    return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
print(nums)

# No credit on leetcode
# Type error
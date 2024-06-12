
def removeElement(nums, val):
    if nums:
        repeat = True
        counter = 0

        while(repeat):
            if len(nums) == 1:
                if nums[0] == val:
                    nums.pop()
                    return 0
                print(nums)
                return 1
            elif val in nums:
                nums.remove(val)
            elif counter == len(nums)-1:
                repeat = False
            else:
                counter += 1

        print(nums)
        return len(nums) - nums.count(val)
    else:
        return 0



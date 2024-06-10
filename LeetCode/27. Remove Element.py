
def removeElement(nums, val):
    if nums:
        repeat = True
        counter = 0

        while(repeat):
            if val in nums:
                nums.remove(val)
            elif counter == len(nums)-1:
                repeat = False
            else:
                counter += 1

        return len(nums) - nums.count(val)
    else:
        print("none")
        return 0

removeElement([], 1)
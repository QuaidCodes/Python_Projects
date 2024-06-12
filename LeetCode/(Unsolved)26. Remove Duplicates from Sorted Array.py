def removeDuplicates(nums):
    def removeNums(nums):
        # print(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    nums.remove(nums[i])
                    removeNums(nums)

                if j >= len(nums) - 1:
                    break

            if i == len(nums) - 1:
                return len(nums)

    return removeNums(nums)

print(removeDuplicates([1,1,2]))
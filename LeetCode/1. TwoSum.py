# 1. Two Sums

def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]


nums = [2, 5, 5, 11]
target = 10

print(twoSum(nums, target))

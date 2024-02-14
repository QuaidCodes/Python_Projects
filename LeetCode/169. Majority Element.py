
# 169. Majority Element

from collections import Counter

def majorityElement(nums):

    occurences = Counter(nums)

    for i, n in enumerate(nums):
        if occurences[n] > len(nums)/2:
            return n



majorityElement([8,8,7,7,7])

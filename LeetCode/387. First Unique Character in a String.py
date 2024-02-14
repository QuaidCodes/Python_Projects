
# 387. First Unique Character in a String

from collections import Counter

def firstUniqChar(s):
    occurences = Counter(s)

    for index, letter in enumerate(s):
        if occurences[letter] == 1:
            return index

    return -1


print(firstUniqChar("aas"))


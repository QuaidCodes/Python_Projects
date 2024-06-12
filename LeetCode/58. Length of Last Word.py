
def lengthOfLastWord(word):
    split_list = word.split(" ")

    for i in reversed(range(len(split_list))):
        if len(split_list[i]) == 0:
            split_list.pop(i)
        else:
            break

    return len(split_list[-1])

print(lengthOfLastWord("   fly me   to   the moon  "))

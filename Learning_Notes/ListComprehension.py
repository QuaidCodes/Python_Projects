
# List comprehension

friends = ["Ajay", "Me", "Myself", "I"]


#newlist = [expression for item in iterable if condition == True]

new_list = [x for x in friends if "Ajay" in x]

print(new_list)

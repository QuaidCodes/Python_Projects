
# 66. Plus One

def plusOne(digits):
    num_str = ""

    for i in digits:
        num_str += (str(i))

    num_int = int(num_str) + 1
    num_str = str(num_int)

    arr = []

    for i in range(len(num_str)):
        arr.append(int(num_str[i]))

    return arr

plusOne([9])

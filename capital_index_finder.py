# Capital Index Finder

def capital_index_finder(str_para):
    index = []
    for i in range(len(str_para)):
        # isupper() returns true if capital
        if str_para[i].isupper():
            index.append(i)

    return index

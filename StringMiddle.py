
# Middle of string finder
def mid(str_para):
    if len(str_para) % 2 == 0:
        return ""
    else:
        middle = len(str_para) / 2
        return str_para[int(middle)]

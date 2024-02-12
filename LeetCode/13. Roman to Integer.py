# 13. Roman to Integer


def romanToInt(s):
    integer = 0

    if "CM" in s:
        integer += 900
        s = s.replace("CM", "")
    if "CD" in s:
        integer += 400
        s = s.replace("CD", "")
    if "XC" in s:
        integer += 90
        s = s.replace("XC", "")
    if "XL" in s:
        integer += 40
        s = s.replace("XL", "")
    if "IX" in s:
        integer += 9
        s = s.replace("IX", "")
    if "IV" in s:
        integer += 4
        s = s.replace("IV", "")

    for i in s:
        if i == "M":
            integer += 1000
        if i == "D":
            integer += 500
        if i == "C":
            integer += 100
        if i == "L":
            integer += 50
        if i == "X":
            integer += 10
        if i == "V":
            integer += 5
        if i == "I":
            integer += 1

    return integer

romanToInt("III")



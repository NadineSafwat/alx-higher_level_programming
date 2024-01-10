#!/usr/bin/python3
def sub(numlst):
    subtract = 0
    lstmax = max(numlst)
    for i in numlst:
        if lstmax > i:
            subtract = subtract + i
    return (lstmax - subtract)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    ndic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keyslst = list(ndic.keys())
    n = 0
    romnum = 0
    numlst = [0]
    for char in roman_string:
        for num in keyslst:
            if num == char:
                if ndic.get(char) <= romnum:
                    n = n + sub(numlst)
                    numlst = [ndic.get(char)]
                else:
                    numlst.append(ndic.get(char))
                romnum = ndic.get(char)
    n = n + sub(numlst)
    return (n)

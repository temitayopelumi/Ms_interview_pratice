import sys


def findMin(str, l, h):
    if l > h:
        return sys.maxsize
    if l == h:
        return 0
    if l == h - 1:
        if str[l] == str[h]:
            return 0
        else:
            return 1

    if str[l] == str[h]:
        print(str[l])
        return findMin (str, l + 1, h + 1)
    else:
        return min (findMin (str, l, h - 1), findMin (str, l + 1, h))+1


print(findMin ('abcd', 0, len ('abcd') - 1))

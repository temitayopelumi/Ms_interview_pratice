def findSub(li,  target):
    for i in range(0, len(str)-1):
        res = 0
        for j in range(i, len(str)-2):
            res+=str[j]
            if res == target:
                count+=1
    return count
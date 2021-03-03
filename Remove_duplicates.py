# def RemoveDuplicates(li):
li = 'geeksforgeeks'
j = 0
for i in range(0, len(li)):
    if li[i] in li[:j]:
        pass
    else:
        li[j] = li[i]
        j = j + 1
print(li[:j])

# g = RemoveDuplicates("geeksforgeeks")
# print(g)

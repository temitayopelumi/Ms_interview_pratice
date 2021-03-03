def Convert(li):
    # to make a sorted list a wave.  we will take two   adjancent numbers and swap them. then go to the next numbers.
    # if we have just 1 left we maintain it

    for i in range(0, len(li)-1, 2):
        li[i], li[i+1] = li[i+1],  li[i]
    return li

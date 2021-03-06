def multiply(num1, num2):
    len1 = len(num1)
    len2 = len(num2)

    if len1 == 0 or len2 == 0:
        return '0'
    result = [0]*(len1  + len2)
    itr1  = 0
    itr2 = 0
    for i in range(len1-1, -1,  -1):
        carry = 0
        n1 = num1[i]
        itr2 = 0
        for j in range(len2-1, -1, -1):
            n2=num2[j]
            summ=n1*n2+result[itr1+itr2]+carry
            carry = summ//10
            result[itr1+itr2]=summ%10
            itr2+=1
        if carry > 0:
            result[itr1+itr2]+=carry
        itr1+=1
        #result in reverse order
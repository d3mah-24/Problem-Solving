for _ in range(int(input())):
    x=input()
    res="No"
    for a in range(len(x)//2-1): 
        if x[a]!=x[a+1]:
            res="Yes"
    print(res)
 
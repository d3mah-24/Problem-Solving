for _ in range(int(input())):
    res=0
    x,y=map(int,input().split())
    mi=min(x,y)
    if (y+x)//4<=mi:
        print((y+x)//4)
    else:
        print(mi)
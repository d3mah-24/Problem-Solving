from functools import reduce
for _ in range(int(input())):
    n=int(input())
    result=-1
    x=list(map(int,input().split()))
    li=[]
    q=1
    for b in x:
       q=b*q 
       li.append(q)
    for c in range(len(x)-1):
        if q/li[c]==li[c]:
            result=c+1
            break
    print(result)



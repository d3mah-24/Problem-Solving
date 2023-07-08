n,k=list(map(int,input().split()))
x=sorted(map(int,input().split()))[::-1]
r=x[k-1]
if r!=0:
    s=x[k:].count(r)
    print(s+k)
else:
    print(x.index(0))
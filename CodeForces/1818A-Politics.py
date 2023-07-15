for _ in range(int(input())): 
    n,k = list(map(int, input().split()))
    s1,s2="",""
    ans = n
    for i in range(n): 
        if not i: 
            s1=input()
        else: 
            s2=input()
            if  s1 != s2 :
                ans-=1
 
    print(ans)
from math import sqrt
    
    
def isprime(temp):
    for i in range(2, int(sqrt(temp)) + 1):
        if temp % i == 0:
            return False
    return True
n=10*5
prime = [True for i in range(n+1)]
p = 2
while (p * p <= n):
    if (prime[p] == True):
        for i in range(p * p, n+1, p):
            prime[i] = False
    p += 1 
for _ in range(int(input())): 
    x=int(input())
    for m in range(2,n+1):
        if prime[m]:
            # print(m,9000)
            if not isprime(x+m):
                break
    print(m)
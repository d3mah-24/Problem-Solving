for _ in range(int(input())):
    n, k, x = map(int, input().split())
    if (k == x == 1):
        print('NO')
    elif (k == 2 and x == 1 and n % 2 == 1):
        print('NO')
    else:
        print('YES')
        if (x != 1):
            print(n)
            a = [1]*n
            print(*a)
        elif (n % 2 == 0):
            print(n//2)
            a = [2]*(n//2)
            print(*a)
        else:
            print(n//2)
            a = [2]*(n//2)
            a[-1] += 1
            print(*a)

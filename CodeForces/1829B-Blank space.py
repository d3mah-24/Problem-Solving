

for _ in range(int(input())):
    input()
    x = [int(y) for y in input().split()]
    m = 0
    t = 0
    for a in x:
        if a == 0:
            t += 1
        else:
            t = 0
        m = max(t, m)
    print(m)

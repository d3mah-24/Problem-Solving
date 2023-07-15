for _ in range(int(input())):
    x = input()
    a = "codeforces"
    z = 0
    for t in range(len(x)):
        if a[t] != x[t]:
            z += 1
    print(z)

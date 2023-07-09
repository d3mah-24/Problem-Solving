for _ in range(int(input())):
    x=input()
    if len(x)<11:
        print(x)
    else:
        print(f"{x[0]}{len(x)-2}{x[-1]}")
 
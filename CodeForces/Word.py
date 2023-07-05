a = input()
u, l = 0, 0
for s in a:
    if s.isupper():
        u += 1
    else:
        l += 1
if l >= u:
    print(a.lower())
else:
    print(a.upper())

st = "qwertyuiopasdfghjkl;zxcvbnm,./"
Direction = input()
l = []
for a in input():
    if Direction == "R":
        l.append(st[st.index(a)-1])
    else:
        l.append(st[st.index(a)+1])
print("".join(l))
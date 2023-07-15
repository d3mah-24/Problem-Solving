d = ["January", "February", "March", "April",  "May", "June",
     "July", "August", "September", "October", "November", "December"]
m = input()
k = int(input())
x = k+d.index(m)
print(d[x % 12])

# 4
# 4
# 11 13 11 11
# 5
# 1 4 4 4 4
# 10
# 3 3 3 3 10 3 3 3 3 3
# 3
# 20 20 10

for _ in range(int(input())):
    input()
    Num_lists=[int(xp) for xp in input().split()]
    Unique_num=sorted(Num_lists,key=lambda c:Num_lists.count(c) )[0]
    print(Num_lists.index(Unique_num))


    
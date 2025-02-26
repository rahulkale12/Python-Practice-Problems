# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n= 5
for i in range(n+1):
    for j in range(i):
        print(i,end = " ")
    print()




# number increment by 1 at everystep 
# 1             1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = 5
num = 1
for i in range(n+1):
    for j in range(i):
        print(num, end = " ")
        num +=1
    print()
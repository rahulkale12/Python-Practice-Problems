# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

n = 5
for i in range(n+1,0,-1):
    for j in range(i):
        print(i,end = " ")
    print()




# decreased at everystep by 1

#15 14 13 12 11
# 10 9 8 7
# 6 5 4
# 3 2
# 1
n = 5
num = sum(range(1, n+1))  

for i in range(n, 0, -1):  
    for j in range(i):
        print(num, end=" ")
        num -= 1  
    print()


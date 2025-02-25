#even

n = 8
for i in range(n):
    for j in range(i):
        if i%2==0:
            print("*",end = " ")
    print()



#odd

n = 8
for i in range(n):
    for j in range(i):
        if i%2!=0:
            print("*",end = " ")
    print()
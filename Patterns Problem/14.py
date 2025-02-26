n = 5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end = " ")
    for j in range(i):
        print(i,end = " ")
    print()


# numbers increasing at every step 1 2 3 4

n = 5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end = " ")
    for j in range(1,i+1):
        print(j,end = " ")
    print()

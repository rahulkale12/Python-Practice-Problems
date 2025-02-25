# even

n = 8
for i in range(n):
    for j in range(n-i):
        print(" ",end = "")
    for j in range(i):
        if i%2==0:
            print("*",end = " ")
    print()



#Odd

n = 6
for i in range(n):
    for j in range(n-i):
        print(" ",end = "")
    for j in range(i):
        if i%2!=0:
            print("*",end = " ")
    print()
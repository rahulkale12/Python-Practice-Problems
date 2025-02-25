n = 5
for i in range(n):  #initial vlaue = 0
    for j in range(n-i-1):   # 4
        print(" ",end = "")
    for j in range(2*i+1):
        print("*",end = "")
    print()

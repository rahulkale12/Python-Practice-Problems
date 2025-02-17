#8.Rotate a List to the Left by n Positions:

a= [1,2,3,4,5]
n =3
n = n% len(a)
print(a[n:]+a[:n])
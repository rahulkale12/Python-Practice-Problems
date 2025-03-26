def fib_range(start,end):
    a,b = 0,1
    while a<=end:
        if a>= start:
            print(a, end = " ")
    a,b = b , a+b

fib_range(10,20)

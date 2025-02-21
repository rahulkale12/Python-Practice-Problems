#7.Create a Nested Dictionary Where the Outer Keys Are Numbers from 1 to 3 and the Inner Dictionary Contains Their Square and Cube:

z = {x:{"square": x**2,"cube":x**3} for x in range(1,4)}
print(z)

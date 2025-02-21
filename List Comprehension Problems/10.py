#10.Generate a 3x3 Matrix Where Each Element is the Product of Its Row and Column Indices (Nested List Comprehension):

z = [[i*j for j in range(3)]  for i in range(3)]
print(z)
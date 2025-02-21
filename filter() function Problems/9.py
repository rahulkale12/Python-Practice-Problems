#9.Use filter() to Remove All Empty Strings from a List: ["python", "", "filter", "reduce", ""]:

l = ["python", "", "filter", "reduce", ""]

z = list(filter(lambda x : x != "",l))
print(z)
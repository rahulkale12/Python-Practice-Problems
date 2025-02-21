#9.Create a Dictionary Where the Keys Are Words in a String and the Values Are Their Reverse:

sentence = "hello world python"

z = {x:x[::-1] for x in sentence.split()}
print(z)
#2.Create a Lambda Function to Check if a Given String Starts with a Vowel:

z = lambda x: x[0].lower() in "aeiou"
print(z("Animal"))
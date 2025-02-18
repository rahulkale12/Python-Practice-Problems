#8.Count the Frequency of Each Character in a String Using a Dictionary:

name = "Raahul"
frequency = {}
for char in name:
    if char in frequency:
        frequency[char] +=1
    else:
        frequency[char]=1

print(frequency)
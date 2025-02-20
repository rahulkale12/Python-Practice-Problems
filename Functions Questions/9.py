#9.Create a Function That Takes a String as Input and Returns It Reversed:



def reverse_str(my_str):
    new =""
    for char in my_str:
        new = char + new

    return new
print(reverse_str("Rahul Kale")) 



# second way using slicing
def reverse_str(my_str):
    return my_str[::-1]

my_str = "Rahul is great"
print(reverse_str(my_str))



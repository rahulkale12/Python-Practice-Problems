#1.Check if a String is a Palindrome:

my_str = "moM"
if my_str.lower() == my_str.lower()[::-1]:
    print("palindrome")
else:
    print("not palindrome")
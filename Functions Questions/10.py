#10.Swap All words in a string except middle one.


def swap_words(my_str):
    word = my_str.split()
    n = len(word)

    mid = n//2
    left =0
    right = n-1

    while left<right:
        if left == mid or right == mid:
            left +=1
            right -=1
        word[left], word[right] = word[right],word[left]

        left +=1
        right -=1

    return " ".join(word)

my_str = "I am in love with python"
print(swap_words(my_str))




# swap only first and last word

# def swapfirst_last(my_str):
#     word =  my_str.split()
#     if len(word)<=2:
#         return my_str
#     word[0],word[-1] = word[-1],word[0]

#     return " ".join(word)

# my_str = "I am in love with python"
# print(swapfirst_last(my_str))




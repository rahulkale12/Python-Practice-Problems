#7.Create a Function to Count the Number of Words in a String:

# def Count_words(my_str):
#     name = my_str.split()
    
#     return len(name)

# print(Count_words("Hello rahul, nice to meet you!!"))


# to calculate each total letetr in each word and total letters in whole string.
# 
def Count(my_str):
    name = my_str.split()
    count_letter_in_word = []
    total_letters = 0
    for word in name:
        count = len(word)
        count_letter_in_word.append(count)
        total_letters+=count

    return len(name),count_letter_in_word,total_letters

my_str=  "Hello rahul, nice to meet you!!"
total,letters,total_letters= Count(my_str)
print(f"Count of total words in string is:{total}")   
print(f"Count of total letters in a word is:{letters}")   
print(f"Count of total letters in string is:{total_letters}")   

 
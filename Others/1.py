#1. words = ["bat", "tab", "king", "kong", "mom", "dad", "mom"]
#output=[0,1,4,6]
#generate python code to check when two string are concatinated and their reverse is comes same (palindrome) 
#and it should return index value of that string.


def find_palindrome(word):
    result =[]
    for i in range(len(word)):
        for j in range(i+1,len(word)):
            if i != j:
                concat = word[i]+word[j]
                if concat == concat[::-1]:
                    result.append(i)
                    result.append(j)
                    break
    return result

word =["bat", "tab", "king", "kong", "mom", "dad", "mom"]
print(find_palindrome(word))

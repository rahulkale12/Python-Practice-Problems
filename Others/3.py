#3. words = ["temp","tempate","ate","roadster","road","ster"]
#output: ["tempate","roadster"]
#write python code which returns the string in which substring are present.
# In above example temp and ate are prsent in tempate and road and ster is present in roadster.


def find_words(given_words):
    result = []
    for word in given_words:
        for sub in given_words:
            if word != sub and sub in word:
                result.append(word)
                break
    return result

given_words = ["temp","tempate","ate","roadster","road","ster"]
print(find_words(given_words))
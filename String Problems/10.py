#10.Check if Two Strings Are Anagrams:

word1 = "listen"
word2 = "silent"

if sorted(word1) == sorted(word2):
    print("Anagram")
else:
    print("Not Anagram")
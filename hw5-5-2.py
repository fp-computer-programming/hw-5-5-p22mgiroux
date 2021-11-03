# Author: MOG 11/2/21

word = input("What is your six letter word? ")

new_word1 = word[0:1] + "-" + word[2:3] + "-" + word[5:6]
new_word2 = word[1:2] + "-" + word[3:4] + "-" + word[6:7]

print(new_word1)
print(new_word2)

# Author: MOG 11/2/21

word = input("What is your word? ")

if word == word[:: -1]:
  print("The word " + word + " is a palindrome because " + word + " spelled backwards is " + word[:: -1] + ".")
else:
  print("The word " + word + " is not a palindrome because " + word + " spelled backwards is " + word[:: -1] + ".")

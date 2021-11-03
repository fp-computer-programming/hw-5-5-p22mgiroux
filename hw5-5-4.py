# Author: MOG 11/2/21

word1 = input("Please input your first word: ").lower()
word2 = input("Please input your second word: ").lower()
word3 = input("Please input your third word: ").lower()

if word1 < word2:
   if word1 < word3:
      first = word1
      if word2 < word3:
         second = word2
         third = word3
      else:
         second = word3
         third = word2
   else:
      first = word3
      second = word1
      third = word2
else:
   if word2 < word3:
      first = word2
      if word1 < word3:
         second = word1
         third = word3
      else:
         second = word3
         third = word1
   else:
      first = word3
      second = word2
      third = word1
      
print("Alphibetical order: {}, {}, {}.".format(first, second, third))

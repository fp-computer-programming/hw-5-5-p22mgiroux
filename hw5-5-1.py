# Author: MOG 11/2/21

string = input("Enter your string to be cut in 2: ")

length = len(string)
half_length = length // 2

print(string[0:half_length])
print(string[half_length:length])

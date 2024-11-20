#check the palindrome in given input
#str1 = "malayalam"
str1 = input("Enter the Word1: ")
revstrg = str1[::-1]

if str1 == revstrg:
    print("Given word is Palindrome")
else:
    print("Given word is Not a Palindrome")




#Getting input of string and substring for doing the search the index of each occurence

test_str = input("Enter the String For Checking the Occurance: ")
test_sub = input("Enter the Substring for Search"
                 "\n& return the INDEX of each Occurance: ")

# printing original string
print("The original string is : " + test_str)
# printing substring
print("The substring to find : " + test_sub)

Final_index=[]
for x in range(len(test_str)):
    if test_str[x] == test_sub:
        Final_index.append(x)

# printing indexes
print("Index of Substring: " + str(Final_index))

str1 = input("Enter the string: ")
str2 = input("Enter the Second string: ")

print("Enter the string in {} {}".format(str2,str1))
txt = input("Enter the Letter:")
result = ""
for char in txt:
    if 'a'<= txt <='z':
       result = result+ chr(ord(char)-32)
    else:
        result = result + char

print(result)

str1 = input("Enter the Number to Reverse: ")
str2 = int(str1)
print(str1[::-1])
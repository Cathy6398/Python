### 1. Write a Python program to find words which are greater than given length k?
list_of_words = ['Apple', 'bananana', 'kiwi', 'berry', 'almond']
k = int(input("1.Enter the length : "))
output = []
for i in list_of_words:
        if len(i) > k:
            output.append(i)
print(output)

### 2. Write a Python program for removing i-th character from a string?
myStr =  input('2.Enter the string : ')
i = int(input('Enter the character to be removed : '))
resStr = myStr.replace(myStr[i-1], "", 1)
print ("String formed by removing i'th character : " + resStr)

### 3. Write a Python program to split and join a string?
string = "3.Write a Python program to split and join a string?"
s = string.split(' ')
print(s)
j = ' '.join(s)
print(j)

### 4. Write a Python to check if a given string is binary string or not?
myStr =  input('4.Enter the string : ')
binary = {'0', '1'}
str = set(myStr)
if binary == str or str == {'0'} or str == {'1'}:
    print("Binary")
else:
    print("Not Binary")

### 5. Write a Python program to find uncommon words from two Strings?

str1 = input('5.Enter first string : ')
str2 = input('Enter second string : ')
S1 = str1.split()
S2 = str2.split()
uncommonWords = set(S1).symmetric_difference(set(S2))
print("Uncommon words are ", uncommonWords)

### 6. Write a Python to find all duplicate characters in string?
string="My name is Kiruba Catherine"
duplicate = []
for i in string:
    if string.count(i) > 1:
        duplicate.append(i)
print("6.",set(duplicate))

### 7. Write a Python Program to check if a string contains any special character?
import re
string = input("7.Enter a string : ")
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  
if(regex.search(string) == None):
    print("Given string does not contain special characters")
else:
    print("Given string contains special characters")


Solution:
       
1.Enter the length : 6
['bananana']
2.Enter the string : Kiruba
Enter the character to be removed : 2
String formed by removing i'th character : Kruba
['3.Write', 'a', 'Python', 'program', 'to', 'split', 'and', 'join', 'a', 'string?']
3.Write a Python program to split and join a string?
4.Enter the string : 01010
Binary
5.Enter first string : My name is Kiruba
Enter second string : My name is Kiruba Catherine
Uncommon words are  {'Catherine'}
6. {' ', 'n', 'e', 'r', 'a', 'i'}
7.Enter a string : kiruba@gmail.com
Given string contains special characters

### 1. Write a program that calculates and prints the value according to the given formula:
import math
def calculate_formula(args):
    c = 50
    h = 30
    result = []
    for d in args:
        result.append(int(math.sqrt((2*c*int(d))/h)))
    print(result)
    
i = list(input("1.Enter comma separated numbers input: ").split(','))
calculate_formula(i)

### 2. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
x=int(input("2.Enter the X value: "))
y=int(input("Enter the y value: "))
matrix=[]
for i in range(x):
    row=[]
    for j in range(y):
        row.append(i*j)
    matrix.append(row)
print(matrix)

### 3. Write a program that accepts a comma separated sequence of words as input and prints 
# the words in a comma-separated sequence after sorting them alphabetically.
i = list(input("3.Enter comma separated word as input: ").split(','))
i.sort()
print(','.join(i))

### 4. Write a program that accepts a sequence of whitespace separated words as input and prints 
# the words after removing all duplicate words and sorting them alphanumerically.
i = list(set(input("4.Enter the white space seperated words as input: ").split(' ')))
i.sort()
print(' '.join(i))

### 5. Write a program that accepts a sentence and calculate the number of letters and digits.
k=input("5.Enter the sentence")
digits=0
letters=0
for c in k:
    if(ord(c) >= ord('a') and ord(c) <= ord('z') or ord(c) >= ord('A') and ord(c) <= ord('Z')):
         letters=letters+1
    elif(ord(c) >= ord('0') and ord(c)<= ord('9') ):
        digits=digits+1

print("The number of letters {}".format(letters))
print("the number of digits {}".format(digits))


Solution:
    
1.Enter comma separated numbers input: 12,20,30
[6, 8, 10]
2.Enter the X value: 2
[[0, 0, 0], [0, 1, 2]]
3.Enter comma separated word as input: my,name,is,kiruba,catherine
catherine,is,kiruba,my,name
4.Enter the white space seperated words as input: my name is kiruba catherine
catherine is kiruba my name
5.Enter the sentence hello world! 123
The number of letters 10
the number of digits 3

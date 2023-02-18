### 1. Write a Python Program to Add Two Matrices?
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
print("1.Addition")
for r in result:
    print(r)

### 2. Write a Python Program to Multiply Two Matrices?
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] * Y[i][j]
print("2.Multiplication")
for r in result:
    print(r)

### 3. Write a Python Program to Transpose a Matrix?
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
print("3.Transpose")
for r in result:
    print(r)

### 4. Write a Python Program to Sort Words in Alphabetic Order?
try:
    my_str = input("4.Enter a string: ")  
    words = my_str.split()  
    words.sort()  
    for word in words:  
        print(word)

except Exception as e:
    print(e)

### 5. Write a Python Program to Remove Punctuation From a String?

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string = input("5.Enter the string: ")
outputString = ""

for char in string:
    if char not in punctuations:
        outputString += char
        
print(outputString)
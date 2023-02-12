### 1. Write a Python Program to Find LCM?
d1=int(input("Enter the 1st digit : "))
d2=int(input("Enter the 2nd digit : "))
if d1 > d2:
    greater = d1
else:
    greater = d2

while(True):
       if((greater % d1 == 0) and (greater % d2 == 0)):
           lcm = greater
           break
       greater += 1

print("L.C.M is",lcm)

### 2. Write a Python Program to Find HCF?
d1=int(input("Enter the 1st digit : "))
d2=int(input("Enter the 2nd digit : "))
if d1 < d2:
    small = d1
else:
    small = d2

for i in range(1, small+1):
       if((d1%i == 0) and (d2 % i == 0)):
           hcf = i
     
print("H.C.F is",hcf)

### 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
d = int(input("\n Enter any decimal number: "))
print(" Binary Number: ", bin(d))
print(" Octal Number: ", oct(d))
print(" Hexadecimal Number: ", hex(d))

### 4. Write a Python Program To Find ASCII value of a character?
char=str(input("Enter the Character : "))
print("ASCII Value of ",char," is :",ord(char))

### 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
m = int(input("Enter any 1st number: "))
n = int(input("Enter any 1st number: "))

print("\nFor addition:       +")
print("For subtraction:    -")
print("For multiplicaton:  *")
print("For division:       /")

ch =str(input("Enter the Operation"))
if(ch == '+'):
    out=m+n
elif(ch == '-'):
    out=m-n
elif(ch == '*'):
    out=m*n
elif(ch == '/'):
    out=m/n

print("Result:",out)


Solution:
1.Enter the 1st digit : 54
Enter the 2nd digit : 24
L.C.M is 216

2.Enter the 1st digit : 54
Enter the 2nd digit : 24
H.C.F is 6

3.Enter any decimal number: 5
 Binary Number:  0b101
 Octal Number:  0o5
 Hexadecimal Number:  0x5
4.Enter the Character : E
ASCII Value of  E  is : 69
5.Enter any 1st number: 32
Enter any 1st number: 12

For addition:       +
For subtraction:    -
For multiplicaton:  *
For division:       /
For Exit:            X
Enter the Operation*
Result: 384
    

### 1. Write a Python Program to Find the Factorial of a Number?
import math


num = int(input("Enter a number to Find the Factorial of a Number: "))
fact = 1
for i in range(num, 0, -1):
    fact = fact*i
print("\nFactorial of",num ,"is",fact)

### 2. Write a Python Program to Display the multiplication Table?
num = int(input("Enter a number for table: "))
for i in range(1, 11):
    print(num,"x",i, "=", num*i)

### 3. Write a Python Program to Print the Fibonacci sequence?
l = 5
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, l ):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

### 4. Write a Python Program to Check Armstrong Number?
n=int(input("\nEnter the number to Check Armstrong Number"))
tmp=n
s=0
while(n>0):
    r = n % 10
    s=s+(r*r*r)
    n = n / 10

if(sum == int(tmp)):
    print("Its Armstrong Number")
else:
    print("Its Not Armstrong Number")

### 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
def fibo(a,b,c):
    if c > 0:
        c -= 1
        print(a, end=' ')
        temp = b
        b = a + b
        a = temp
        fibo(a,b,c)
fibo(0,1,10)

### 2. Write a Python Program to Find Factorial of Number Using Recursion?
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num=int(input("\nEnter the number : "))
print("The factorial of", num, "is", factorial(num))

### 3. Write a Python Program to calculate your Body Mass Index?
def bmi(height, weight):
    
    calc=weight/(height*height)
    return calc

w=int(input("Enter the weight in Kg : "))
h=int(input("Enter the height in meters : "))

print("The BMI is ", bmi(h,w))

### 4. Write a Python Program to calculate the natural logarithm of any number?
import math
num = int(input("\nEnter the number to calculate the natural logarithm: "))
print(math.log(num))

### 5. Write a Python Program for cube sum of first n natural numbers?
def cub(n):
    return sum(range(n+1))**3

s=int(input("\nEnter the number to  cube sum of first n natural numbers"))
print("Result is ",cub(s))



Solution:
    
1.0 1 1 2 3 5 8 13 21 34 
2.Enter the number : 6
The factorial of 6 is 720
3.Enter the weight in Kg : 55
Enter the height in meters : 160
The BMI is  0.0021484375

4.Enter the number to calculate the natural logarithm: 14
2.6390573296152584

5.Enter the number to  cube sum of first n natural numbers4
Result is  1000

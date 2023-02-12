### 1. Write a Python Program to Find the Factorial of a Number?
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
num = int(input("\nEnter a number to Check Armstrong Number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

### 5. Write a Python Program to Find Armstrong Number in an Interval?
low = int(input("Enter the lower value of range: "))
high = int(input("Enter the higher value of range: "))

for num in range(low, high + 1):
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

   if num == sum:
       print(num)

### 6. Write a Python Program to Find the Sum of Natural Numbers?
h=int(input("Enter the number to Find the Sum of Natural Numbers"))
tmp=0
for i in range(1,h+1):
    tmp=tmp+i
print(tmp)


Solution:
1.Enter a number to Find the Factorial of a Number: 3

Factorial of 3 is 6

2.Enter a number for table: 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

3.Fibonacci Series: 0 1 1 2 3
   
4.Enter a number to Check Armstrong Number: 371
371 is an Armstrong number

5.Enter the lower value of range: 1
Enter the higher value of range: 1000
1
153
370
371
407

6.Enter the number to Find the Sum of Natural Numbers5
15

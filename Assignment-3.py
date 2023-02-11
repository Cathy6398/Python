### 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
a=int(input("Enter the Number to Check if a Number is Positive, Negative or Zero: "))
if(a > 0):
   print(a,"is Positive")
elif(a < 0):
   print(a,"is Negative")
else:
   print(a,"is Zero")

### 2. Write a Python Program to Check if a Number is Odd or Even?
n=int(input("Enter the Number to Check if a Number is Odd or Even: "))
if(n % 2 ==0):
  print(n,"is Even")
else:
    print(n,"is odd")

### 3. Write a Python Program to Check Leap Year?
year = int(input("Enter a number to Check Leap Year: "))
if(year % 4 == 0):
    print(year,"its Leap Year")
else:
   print(year,"its Not Leap Year")

   
   
   
   
   Solution
Enter the Number to Check if a Number is Positive, Negative or Zero: 0
0 is Zero
Enter the Number to Check if a Number is Odd or Even: 90
90 is Even
Enter a number to Check Leap Year: 1957
1957 its Not Leap Year


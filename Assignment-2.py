### 1. Write a Python program to convert kilometers to miles?
Km=5
miles = 0.62137*Km
print("Converting ",Km," Km to Miles is :",miles);
### 2.Write a Python program to convert Celsius to Fahrenheit?
Celsius=9
Fahrenheit=Celsius*9/5+32
print("Value of converting ",Celsius,"Celsius to Fahrenheit is: ",Fahrenheit);
### 3. Write a Python program to display calendar?
import calendar
year=2023
print(calendar.calendar(year))
### 4. Write a Python program to solve quadratic equation?
import math
a = int(input(("Enter the a: ")))
b = int(input(("Enter the b: ")))
c = int(input(("Enter the c: ")))
d = (b**2) - (4*a*c)
print(d)

q1 = ((-1*b)+(math.sqrt(d))) / (2*a)
q2 = ((-1*b)-(math.sqrt(d))) / (2*a)

print('\nFor quad eq. {}x^2 + ({})x^1 + {}'.format(a,b,c))
print('The solutions are: {} and {}'.format(q1, q2))

### 5. Write a Python program to swap two variables without temp variable?
a=8
b=7
print("Before swap a : ",a ,"b: ",b)
a=a+b
b=8
a=a-b
print("After swap a : ",a ,"b: ",b)


Solution:
  
1.Converting  5  Km to Miles is : 3.1068499999999997
  
2.Value of converting  9 Celsius to Fahrenheit is:  48.2
  
 3.                                 2023

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5             1  2  3  4  5
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
23 24 25 26 27 28 29      27 28                     27 28 29 30 31
30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7                1  2  3  4
 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                   1  2  3
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                   1  2  3
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10

4.Enter the a: 1
Enter the b: -9
Enter the c: 14
25

For quad eq. 1x^2 + (-9)x^1 + 14
The solutions are: 7.0 and 2.0

5. Before swap a :  8 b:  7
After swap a :  7 b:  8
PS C:\Users\kirub>

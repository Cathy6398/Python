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
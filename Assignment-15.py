### 1. Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n 
#in comma separated form while n is input by console.
def division(n):
    
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield (str(i)+' ')

n=int(input("1.Enter the N value : "))
division(n)
print(', '.join([i for i in division(n)]))

### 2. Please write a program using generator to print the even numbers between 0 and n in comma separated form while n 
# is input by console.
def EvenNo(n):
    for i in range(n+1):
        if(i%2 == 0):
            yield (str(i)+' ')

n=int(input("2.Enter the N value : "))
EvenNo(n)
print(' '.join([i for i in EvenNo(n)]))

### 3. Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n 
# input by console.
def fibonacci(n):
    i = 0
    j = 1
    for k in range(n+1):
        yield i
        i,j = j, i+j

n=int(input("3.Enter the N value : "))
fibonacci(n)
print(','.join([str(num) for num in fibonacci(n)]))

### 4. Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print
#  the user name of a given email address. Both user names and company names are composed of letters only.
email = str(input("4.Enter the email address : "))
email = email.split('@')
print(email[0])

### 5. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
#  Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length
print("5.")
n=int(input("Enter the Value to calculate the area : "))
Asqr = Square(n)
print("The Area is ",Asqr.area())


Solution:
    
1.Enter the N value : 100
0 , 35 , 70
2.Enter the N value : 10
0  2  4  6  8  10
3.Enter the N value : 5
0,1,1,2,3,5
4.Enter the email address : kiruba@gmail.com
kiruba
5.Enter the Value to calculate the area : 4
The Area is  16

### 1. Write a Python program to check if the given number is a Disarium Number?
num = int(input("1.Enter the Number : "))
rem = s = 0
len = len(str(num))
n = num
while(num > 0):
    rem = num%10
    s += int(rem**len)
    num = num//10
    len =len - 1
if(s == n):  
    print( "Disarium number")
else:
    print(" Not a Disarium number")

### 2. Write a Python program to print all disarium numbers between 1 to 100?
def Disarium(num):
    rem=sum = 0
    l = len(str(num))
    while(num>0):
        rem = num%10
        sum= sum + rem**l  
        l=l-1
        num = num//10
    return sum

print("2.Disarium no in range 1 to 100")
disno = []
for i in range(1,101):
    sum = 0
    sum = Disarium(i)
    if sum == i:
        disno.append(i)        
print(disno)

### 3. Write a Python program to check if the given number is Happy Number?
def Happy(num):
    sum = 0
    while(num>0):
        rem = num%10
        sum= sum + rem**2        
        num = num//10
    return sum

num = int(input("3.Enter the number :"))
result = num

while (result != 1 and result != 4):
    result = Happy(result)

if result == 1:
    print(num,"Is a Happy Number")
else:
    print(num," Is a Unhappy Number")

### 4. Write a Python program to print all happy numbers between 1 and 100?
def Happy(num):
    rem=sum = 0
    while(num>0):
        rem = num%10
        sum= sum + rem**2  
        num = num//10
    return sum

print("4.Happy Number no in range 1 to 100")

happyNo = []

for i in range(1,101):
    result =i  
    while (result != 1 and result != 4):
        result = Happy(result)
    if result == 1:
        happyNo.append(i)
print(happyNo)

### 5. Write a Python program to determine whether the given number is a Harshad Number?
def digsum(num):
    sum = 0
    while(num>0):
        rem = num%10
        sum= sum + rem      
        num = num//10
    return sum

num = int(input("5.Enter the number : "))
sum = digsum(num)

if num % sum == 0:
    print(num,"Is a Harshad number")
else:
    print(num,"Is not a Harshad number")

### 6. Write a Python program to print all pronic numbers between 1 and 100?
def PronicNo(num):
    Pronic = False
    for i in range(1,num+1):
        if i*(i+1) == num:
            Pronic = True
            break
    return Pronic

print("6.Pronic numbers in range 1 to 100")
pronicno = []
for i in range(1,101):
    if PronicNo(i):
        pronicno.append(i)
print(pronicno)

Solution
1.Enter the Number : 175
Disarium number
2.Disarium no in range 1 to 100
[1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
3.Enter the number :19
19 Is a Happy Number
4.Happy Number no in range 1 to 100
[1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]
5.Enter the number : 21
21 Is a Harshad number
6.Pronic numbers in range 1 to 100
[2, 6, 12, 20, 30, 42, 56, 72, 90]

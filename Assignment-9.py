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


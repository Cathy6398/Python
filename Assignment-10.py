### 1. Write a Python program to find sum of elements in list?
l=[1,2,3,4,5,6,7,8,9]
total=0
for i in l:
    total=total+i
print("1.The Sum is",total)

### 2. Write a Python program to  Multiply all numbers in the list?
l=[1,2,3,4,5]
mul=1
for i in l:
    mul=mul*i
print("2.The Result is",mul)

### 3. Write a Python program to find smallest number in a list?
l=[1,2,3,4,5]
minimum = l[0]
for i in l:
    if i < minimum:
        minimum = i      
print ("3.The minimum value is",minimum)

### 4. Write a Python program to find largest number in a list?
l=[1,2,3,4,5]
maxi = l[0]
for i in l:
    if i > maxi:
        maxi = i
print ("4.The maximum value is",maxi)

### 5. Write a Python program to find second largest number in a list?
l=[10,22,13,40,5]
l.sort()
print ("5.The second largest value is",l[3])

### 6. Write a Python program to find N largest elements from a list?
print("6.The list has 10,22,13,40,5" )
num=int(input("Enter the  N largest elements from a list : "))
l=[10,22,13,40,5]
l.sort(reverse=True)
print ("The",num,"largest value is",l[num-1])

### 7. Write a Python program to print even numbers in a list?
l=[10,22,13,40,5]
print("7.The even numbers in a list are")
for num in l:
    if num % 2 == 0:
        print(num, end=" ")

### 8. Write a Python program to print odd numbers in a List?
l=[10,22,13,40,5]
print("\n8.The odd numbers in a list are")
for num in l:
    if num % 2 == 1:
        print(num, end=" ")

### 9. Write a Python program to Remove empty List from List?
l = [[], 12, 31, [1,2, -23] , [1], [], [123.23], [], 2, 321]
result = []

for i in l:
    if type(i) == list:
        if len(i) != 0:
            result.append(i)
    else:
        result.append(i)

print("\n9.",result)

### 10. Write a Python program to Cloning or Copying a list?
l1=[10,22,13,40,5]
l2=[]

for i in l1:
    l2.append(i)
print("10.",l2)

### 11. Write a Python program to Count occurrences of an element in a list?
l=[10,22,13,10,40,5,10].count(10)
print("11.",l)

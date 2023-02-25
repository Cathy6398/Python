### 1. Write a Python program to Extract Unique values dictionary values?
dict1 = {'k1': 1, 'k2': 1, 'k3': 'hello', 'k4': 'hello', 'k5':1234}
unique_values = {i for i in dict1.values()}
print('1.Unique values values in dictionary',unique_values)

### 2. Write a Python program to find the sum of all items in a dictionary?
dict2 = {'k1' : 89,'k2' : 111, 'k3' : 123,'k4' : 5}
sum=0
for i in dict2.values():
    sum=sum+i
print("2.Sum of all items in a dictionary is {}".format(sum))

### 3. Write a Python program to Merging two Dictionaries?
dict1 = { 'x': 1, 'l': 2}
dict2 = { 'k': 3, 'z': 4, 'y': 11}
for i in dict2.items():
    dict1.setdefault(i[0], i[1])
print("3.",dict1)

### 4. Write a Python program to convert key-values list to flat dictionary?
dict4 = {'month' : [1, 2, 3], 'name' : ['Jan', 'Feb', 'March']}
result=dict(zip(dict4['month'],dict4['name']))
print("4.Flat dictionary:",result)

### 5. Write a Python program to insertion at the beginning in OrderedDict?
from collections import OrderedDict
dict5 = OrderedDict([('Feb', '2'), ('Mar', '3')])
dict5.update({'Jan':'1'})
dict5.move_to_end('Jan',last=False)
print("5.The updated Dictionary is ",dict5)

### 6. Write a Python program to check order of character in string using OrderedDict()?
from collections import OrderedDict 
  
def checkOrderofString(str, pattern):
    dict6 = OrderedDict.fromkeys(str) 
    print(dict6)   
    ptrlen = 0
    for key,value in dict6.items(): 
        
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
          
        if (ptrlen == (len(pattern))):            
            return 'true'
    return 'false'
  
string = input("6.Enter string : ")
pattern = input("Enter Pattern : ")
if checkOrderofString(string,pattern):
    print("Pattern matched")
else:
    print("Pattern not matched")

### 7. Write a Python program to sort Python Dictionaries by Key or Value?
dict7 = {'k1':2, 'k2':1, 'k3':3, '4':4 ,'6':6, 'key7':7}
print("7.Sorted Keys",sorted(dict7.keys()))
print("Sorted Values",sorted(dict7.values()))


Solution:

1.Unique values values in dictionary {'hello', 1, 1234}
2.Sum of all items in a dictionary is 328
3. {'x': 1, 'l': 2, 'k': 3, 'z': 4, 'y': 11}
4.Flat dictionary: {1: 'Jan', 2: 'Feb', 3: 'March'}
5.The updated Dictionary is  OrderedDict([('Jan', '1'), ('Feb', '2'), ('Mar', '3')])
6.Enter string : Catheriene
Enter Pattern : ath
OrderedDict([('C', None), ('a', None), ('t', None), ('h', None), ('e', None), ('r', None), ('i', None), ('n', None)])
Pattern matched
7.Sorted Keys ['4', '6', 'k1', 'k2', 'k3', 'key7']
Sorted Values [1, 2, 3, 4, 6, 7]

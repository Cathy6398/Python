### 1. Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
import zlib

def division(s):
    for i in range(0,s+1):
        if(i%7 == 0):
            print(i)
num=int(input("1.Enter the end range : "))
division(num)

### 2. Write a program to compute the frequency of the words from the input. 
# The output should output after sorting the key alphanumerically.
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print("2.")
print(word_count('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3'))


### 3. Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" 
# which can print "Male" for Male class and "Female" for Female class.
class Person:
    def getGender(self):
        pass
class Male(Person):
    def getGender(self):
        print("3.Male")
class Female(Person):
    def getGender(self):
        print("Female")

m=Male()
f=Female()
m.getGender()
f.getGender()

### 4. Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ['Play', "Love"] and the object is in ["Hockey","Football"].
print("4.")
subject = ["I", "You"] 
verb =['Play', "Love"] 
object = ["Hockey","Football"]
sentence=[]
for i in subject:
    for j in verb:
        for k in object:
            sentence.append(i+" "+j+" "+k)

for(s) in sentence:
    print(s)

### 5. Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!"
text="hello world!hello world!hello world!hello world!"
comp=zlib.compress(bytes(text,'utf-8'))
decomp=zlib.decompress(comp)
print("5.Compressed String : ",comp)
print("Decompress String : ",decomp)

### 6. Please write a binary search function which searches an item in a sorted list. 
# The function should return the index of element to be searched in the list.

def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [2,3, 4, 5, 6, 7, 8, 9]
x = 9
print("6.")
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
    
    
    
Solution:
    
1.Enter the end range : 50
0
7
14
21
28
35
42
49
2.
{'New': 1, 'to': 1, 'Python': 5, 'or': 2, 'choosing': 1, 'between': 1, '2': 2, 'and': 1, '3?': 1, 'Read': 1, '3': 1}
3.Male
Female
4.
I Play Hockey
I Play Football
I Love Hockey
I Love Football
You Play Hockey
You Play Football
You Love Hockey
You Love Football
5.Compressed String :  b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5'
Decompress String :  b'hello world!hello world!hello world!hello world!'
6.
Element is present at index 7

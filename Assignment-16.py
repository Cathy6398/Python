### 1. Write a function that stutters a word as if someone is struggling to read it. 
#The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a
#question mark ?. Examples stutter('incredible') ➞ 'in... in... incredible?' stutter('enthusiastic') ➞ 'en... en... enthusiastic?' 
#stutter('outstanding') ➞ 'ou... ou... outstanding?'
### Hint :- Assume all input is in lower case and at least two characters long.

def slutter(word:str):
    print(f"{word[:2]}... {word[:2]}... {word}?")

print("1.")
slutter("incredible")
slutter("enthusiastic")
slutter("outstanding")

### 2. Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.
def radian(rad):
    return (57.295779513 * rad)
print("2.")
print(radian(3))

### 3. In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 
# plus 2 multiplied by num, then num is a Curzon number. Given a non-negative integer num, implement a function that returns True 
# if num is a Curzon number, or False otherwise.

def curzon(n):
    if (1 + 2 ** n) % (1 + 2*n) == 0:
        print ("True")
    else:
        print("False")
print("3.")
curzon(7)

### 4. Given the side length x find the area of a hexagon.
import math
def areahex(a):
    return(3 * math.sqrt(3) * 0.5 * a* a )
print("4.")
print(areahex(2))

### 5. Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. 
# To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.

def binary(n):
    return "{0:b}".format(int(n))
print("5.")
print(binary(5))



Solution:
1.
in... in... incredible?
en... en... enthusiastic?
ou... ou... outstanding?
2.
171.88733853899998
3.
False
4.
10.392304845413264
5.
101

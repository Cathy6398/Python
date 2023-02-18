### 1. Write a Python Program to find sum of array?
l = [1,2,3,-412, 123, 369, 111]
arraySum = 0
for i in l:
    arraySum += i  
print("1.Sum of array: ", arraySum)

### 2. Write a Python Program to find largest element in an array?
arrayMax = 1000
for i in l:
    if i > arrayMax:
        arrayMax = i
print("2.",arrayMax)

### 3. Write a Python Program for array rotation?
l = [1,2,3,-412, 123, 369, 111]
print("3.Rotated array:",l[::-1])

### 4. Write a Python Program to Split the array and add the first part to the end?
def split(arr, k):
    arr = arr[k:] + arr[:k]
    return arr 
k = 2
arr = [10, 13, 5, 17]
print("4.Output array is", split(arr, k))

### 5. Write a Python Program to check if given array is Monotonic?

def isMonotonic(A):
   return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
      all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
# main
A = [8,1,2,3,4,7,8]
print("5.",isMonotonic(A))


Solution

1.Sum of array:  197
2. 1000
3.Rotated array: [111, 369, 123, -412, 3, 2, 1]
4.Output array is [5, 17, 10, 13]
5. False

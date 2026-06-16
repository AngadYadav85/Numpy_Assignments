"""
# Q1. Array Addition

## Problem Statement
Create two NumPy arrays:

```python
arr1 = [1, 2, 3, 4]
arr2 = [10, 20, 30, 40]
```
"""

import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([10,20,30,40])
result=arr1+arr2
print("Array 1 is ",arr1)
print("Array 2 is ",arr2)
print("Addition of both array is ",result)


"""
# Q2. Array Multiplication

## Problem Statement
Create two NumPy arrays and multiply them element-wise.

## Sample Input
```python
arr1 = [2, 4, 6]
arr2 = [3, 5, 7]
```
"""

import numpy as np
arr1=np.array([2,4,6])
arr2=([3,4,7])
result=arr1*arr2
print("Array 1 is ",arr1)
print("Array 2 is ",arr2)
print("Result of array is ",result)

"""
# Q3. Add a Scalar to an Array

## Problem Statement
Create the array:

```python
[10, 20, 30, 40]
```

Add 5 to every element using broadcasting.

"""

import numpy as np
arr=np.array([10,20,30,40])
result=(arr+5)
print("The Array ",arr)
print("The addition of 5 in every elements is ",result)


"""
# Q4. Multiply Array by a Scalar

## Problem Statement
Multiply every element of the array by 3.

## Sample Input
```python
[1, 2, 3, 4]

"""

import numpy as np
arr=np.array([1,2,3,4])
result=(arr*3)
print("The array is ",arr)
print("The multiplication of 3 in every elementsg is",result)


"""
# Q5. Matrix Broadcasting

## Problem Statement
Create a 2×3 array and add 10 to every element.

## Sample Input
```python
[[1,2,3],
 [4,5,6]]

"""

import numpy as np
arr=np.array([[1,2,3],
              [4,5,6]])
result=(arr+10)
print("The array is",arr)
print("The addition of 10 in every elements is:",result)



"""
# Q6. Find Sum of Array

## Problem Statement
Create the array:

```python
[5, 10, 15, 20]

"""

import numpy as np
arr=np.array([5,10,15,20])
sum=0
for i in arr:
    sum+=i
    print("sum of all elements is ",sum)



"""
# Q7. Find Mean of Array

## Problem Statement
Create the array:

```python
[10, 20, 30, 40, 50]
```
Find the average value.
"""

import numpy as np
arr=np.array([10,20,30,40,50])

# we use the mean inbuilt function  to print the average

average=np.mean(arr)

print("The average of all elements is: ",average)

"""

# Q8. Find Maximum and Minimum Value

## Problem Statement
Create the array:

```python
[12, 45, 7, 89, 23]
```

 Print:
 - Maximum Value
- Minimum Value
 """


import numpy as np
arr=np.array([12,45,89,23])
## here we also use the inbult function of min and max
maximum=np.max(arr)
minimum=np.min(arr)

print("The maximum number is: ",maximum)
print("The minimum  number is: ",minimum)

"""
# Q9. Row-wise Sum using Axis

## Problem Statement
Create the array:

```python
[[1,2,3],
 [4,5,6]]
```

Find row-wise sum using axis.
"""

import numpy as np
arr=np.array([[1,2,3],
              [4,5,6]])

row_sum=np.sum(arr,axis=1) # we use the sum fuctions with the axis=1 , 
print("The sum of elements in row_wise :",row_sum)


"""

# Q10. Column-wise Sum using Axis

## Problem Statement
Create the array:

```python
[[1,2,3],
 [4,5,6]]
```
Find column-wise sum using axis.
"""

import numpy as np
arr=np.array([[1,2,3],
             [4,5,6]])
column_sum=np.sum(arr,axis=0)

print("The sum of column is:",column_sum)


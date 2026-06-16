"""
# Q1. Fancy Indexing (1D Array)

## Problem Statement
Create the array:

```python
[10, 20, 30, 40, 50, 60]
```

Using fancy indexing, print:
- 10
- 30
- 60

## Sample Output
```python
[10 30 60]

"""

import numpy as np
arr=np.array([10,20,30,40,50,60])
result=arr[[0,2,5]]  # this is called the fancy indexing ,we can get the elemnts by using its index
print(result)



"""
# Q2. Fancy Indexing (1D Array)

## Problem Statement
Create the array:

```python
[5, 15, 25, 35, 45]
```

Using fancy indexing, print:
- 15
- 45

## Sample Output
```python
[15 45]
"""


import numpy as np
arr=np.array([5,15,25,35,45])
result=arr[[1,4]]
print(result)

"""
# Q3. Fancy Indexing (2D Array)

## Problem Statement
Create the matrix:

```python
[[10,20,30],
 [40,50,60],
 [70,80,90]]
```

Using fancy indexing, print:
- 10
- 50
- 90

## Sample Output
```python
[10 50 90]
"""

import numpy as np
arr=np.array([[10,20,30],
             [40,50,60],
             [70,80,90]])

result=arr[[0,1,2],[0,1,2]]

print(result)


"""

# Q4. Conditional Selection

## Problem Statement
Create the array:

```python
[5, 12, 18, 25, 30, 7]
```

Print only values greater than 15.

## Sample Output
```python
[18 25 30]

"""

import numpy as np
arr=np.array([5,12,18,25,30,7])
result= arr[arr>15]
print(result)



"""
# Q5. Conditional Selection

## Problem Statement
Create the array:

```python
[2, 4, 7, 10, 13, 16]
```

Print only even numbers.

## Sample Output
```python
[ 2  4 10 16]

"""

import numpy as np
arr=np.array([2,4,7,10,13,16])
result=arr[arr%2==0]
print(result)


"""
# Q6. Sorting an Array

## Problem Statement
Create the array:

```python
[25, 10, 40, 5, 30]
```

Sort the array using `np.sort()`.

## Sample Output
```python
[ 5 10 25 30 40]

"""


import numpy as np 
arr=np.array([5,10,25,30,40])
result=np.sort(arr)
print(result)


"""
<!-- # Q7. Find Sorted Indices

## Problem Statement
Create the array:

```python
[50, 20, 70, 10]
```

Use `np.argsort()` to find the indices of sorted elements.

## Sample Output
```python
[3 1 0 2]

"""

import numpy as np
arr=np.array([50,20,70,10])
result=np.argsort(arr)
print(result)


"""
# Q8. Concatenate Arrays

## Problem Statement
Create two arrays:

```python
arr1 = [1,2,3]
arr2 = [4,5,6]
```

Concatenate both arrays.

## Sample Output
```python
[1 2 3 4 5 6]

"""


import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

result=np.concatenate((arr1,arr2))
print(result)




"""
# Q9. Vertical Stacking

## Problem Statement
Create two arrays:

```python
[1,2,3]
[4,5,6]
```

Combine them using vertical stacking.

## Sample Output
```python
[[1 2 3]
 [4 5 6]]
"""


import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

result=np.vstack((arr1,arr2)) # by using the vstack we can print the vertical way
print(result)


"""
# Q10. Horizontal Stacking

## Problem Statement
Create two arrays:

```python
[10,20,30]
[40,50,60]
```

Combine them using horizontal stacking.

## Sample Output
```python
[10 20 30 40 50 60]

"""

import numpy as np
arr1=np.array([10,20,30])
arr2=np.array([40,50,60])

result=np.hstack((arr1,arr2))
print(result)






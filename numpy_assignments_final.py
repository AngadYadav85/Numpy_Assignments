# """
# # Q1. Array Creation and Attributes

# ## Problem Statement
# Create array [10,20,30,40,50] and print shape, ndim, size and dtype.

# ## Sample Input
# ```python
# Use NumPy arrays
# ```

# ## Sample Output
# ```python
# Expected Output

# """

import numpy as np
arr=np.array([10,20,30,40,50])
print('The array is:',arr)
print('The shape of array is:',arr.shape)
print('The dimesional of array is:',arr.ndim)
print('The size of array is:',arr.size)
print('The datatype array is:',arr.dtype)

"""

# Q2. Matrix Creation

## Problem Statement
Create a 3x3 NumPy matrix and print it.

## Sample Input
```python
Use NumPy arrays
```

## Sample Output
```python
Expected Output
"""

import numpy as np
arr=np.matrix([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(arr)


"""
# Q3. Indexing Practice

## Problem Statement
Print first, third and last element from an array.

## Sample Input
```python
Use NumPy arrays
```

## Sample Output
```python
Expected Output
"""

import numpy as np
arr=np.array([10,20,30,40,50,60])
result=arr[[0,2,-1]]
print(result)



"""
# Q4. Slicing Practice

## Problem Statement
Print elements from index 2 to 5.

## Sample Input
```python
Use NumPy arrays
```

## Sample Output
```python
Expected Output
"""

import numpy as np
arr=np.array([10,20,30,40,50,60,70])
result=arr[2:6]  # slicing by using the start ,stop and step
print(result)



"""
# Q5. Fancy Indexing

## Problem Statement
Print selected elements using fancy indexing.

## Sample Input
```python
Use NumPy arrays
```

## Sample Output
```python
Expected Output
"""


import numpy as np
arr=np.array([10,20,30,40,50])
result=arr[[0,2,4]]  ## we can access the element of specific index by using the fancy indexing 
print(result)



"""
# Q6. Conditional Selection

## Problem Statement
Print values greater than 15.

## Sample Input
```python
Use NumPy arrays
```

## Sample Output
```python
Expected Output
"""

import numpy as np
arr=np.array([3,4,6,18,36,56,70])
result=arr[arr>15]
print(result)



"""
# Q7. Broadcasting

## Problem Statement
Add 10 to every element of an array.

## Sample Input
```python
Use NumPy arrays
```

## Sample Output
```python
Expected Output
"""

import numpy as np
arr=np.array([10,20,30,40,50,70])
result=(arr+10)
print(result)




"""
# Q8. Aggregate Functions

## Problem Statement
Print sum, mean, max and min.

## Sample Input
```python
Use NumPy arrays
```

## Sample Output
```python
Expected Output
"""


import numpy as np
arr=np.array([10,20,30,40,50,60,70])
sum=0
for i in arr:
    sum+=i
average=arr.mean()
maximum=arr.max()
minimum=arr.min()
print("sum is",sum)
print("average is",average)
print(" maximum is",maximum)
print("minimum is",minimum)



"""

# Q9. Sorting

## Problem Statement
Sort an unsorted NumPy array.

## Sample Input
```python
Use NumPy arrays
```

## Sample Output
```python
Expected Output
"""


import numpy as np
arr=np.array([50,30,70,40,20])
result=np.sort(arr)

print(result)


"""
# Q10. Concatenation and Stacking

## Problem Statement
Perform concatenate and vstack on two arrays.

## Sample Input
```python
Use NumPy arrays
```

## Sample Output
```python
Expected Output
"""

import numpy as np
arr1=np.array([1,2,3,4,6])
arr2=np.array([7,8,9,10,11])

# using the concatenate 
concatenate=np.concatenate((arr1,arr2))

vstack=np.vstack((arr1,arr2))


print("The addition is ",concatenate)
print("The vertical order is ",vstack)



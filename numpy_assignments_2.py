""" # Q1. Array Attributes

## Problem Statement
# Create the following NumPy array:

# ```python
# [10, 20, 30, 40, 50]
# ```

# Print:
# - Shape
# - Number of Dimensions
# - Size
# - Data Type"""

# import numpy as np
# arr=[[1,2,3],[4,5,6],[7,8,9]]
# arr=np.array(arr)
# print(arr)
# print(arr.shape) # it prints the number of rows and column
# print(arr.ndim) # it prints the number of dimension
# print(arr.size) # it prints the total number of elements
# print(arr.dtype) # it prints the data types 

"""
# Q2. Find Array Shape

## Problem Statement
Create the following array:

```python
[[1,2,3],
 [4,5,6]]
```
Print only the shape of the array.

"""

# import numpy as np
# arr=[[1,2,3],[4,5,6]]
# arr=np.array(arr)
# print(arr)

# print(arr.shape)

"""
# Q3. 1D Indexing

## Problem Statement
Create the array:

```python
[5, 10, 15, 20, 25]
```

Print:
- First element
- Last element
"""
# import numpy as np
# arr=[5,10,15,20,25]
# arr=np.array(arr)
# print(arr)
# print(arr[0])
# print(arr[-1])

"""
# Q4. 2D Indexing

## Problem Statement
Create the array:

```python
[[10,20,30],
 [40,50,60],
 [70,80,90]]
```

Print the element `50`.
"""

# import numpy as np 
# arr=[[10,20,30],[40,50,60],[70,80,90]]
# arr=np.array(arr)
# print(arr)
# print(arr[1,1])

"""
# Q5. 2D Indexing

## Problem Statement
Create the array:

```python
[[1,2,3],
 [4,5,6],
 [7,8,9]]
```

Print the element `9`.
"""

# import numpy as np
# arr=[[1,2,3],[4,5,6],[7,8,9]]
# arr=np.array(arr)
# print(arr)
# print(arr[2:,2:])

"""
# Q6. 1D Slicing

## Problem Statement
Create the array:

```python
[10,20,30,40,50,60]
```

Print elements from index 1 to 4.
"""

# import numpy as np
# arr=[10,20,30,40,50,60]
# arr=np.array(arr)
# print(arr)
# print(arr[1:5:1])


"""

# Q7. 1D Slicing

## Problem Statement
Create the array:

```python
[1,2,3,4,5,6,7,8]
```

Print the first 5 elements.

"""

# import numpy as np
# arr=[1,2,3,4,5,6,7,8]
# arr=np.array(arr)
# print(arr)
# print(arr[0:5:1])

"""
# Q8. 2D Slicing

## Problem Statement
Create the array:

```python
[[1,2,3],
 [4,5,6],
 [7,8,9]]
```
Print the first two rows.
"""

# import numpy as np
# arr=[[1,2,3],[4,5,6],[7,8,9]]
# arr=np.array(arr)
# print(arr)
# print(arr[0:2,0:3])

"""
# Q9. 2D Slicing

## Problem Statement
Create the array:

```python
[[10,20,30],
 [40,50,60],
 [70,80,90]]
```

Print the first two columns of all rows.
"""

# import numpy as np
# arr=[[10,20,30],[40,50,60],[70,80,90]]
# arr=np.array(arr)
# print(arr)
# print(arr[0:3,0:2])

"""
# Q10. Boolean Indexing

## Problem Statement
Create the array:

```python
[5, 12, 18, 25, 30, 7]
```

Print only the values greater than 15.

"""

# import numpy as np
# arr=[5,12,18,25,30,7]
# arr=np.array(arr)
# print(arr)
# print(arr>15)
# print(arr[arr>15])








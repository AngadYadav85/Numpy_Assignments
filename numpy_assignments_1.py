"""
>>- NUMPY ASSIGNMENT -1 
(1).Import numpy
(02).zeroes()
(03).ones()
(04).full()
(05).arange()
(06).linspace()
(07).eye()
(08).random arrays()

THERE ARE TWO QUESTION GIVEN BELOW 
"""

# (01) Create a numpy array using a list 

import numpy as np
list=[10,20,30,40]
arr=np.array(list)
print(arr)

# (02).Create a matrix the list in python

import numpy as np
list=[[10,20,30],
      [40,50,60],
      [70,80,90]]
arr=np.array(list)
print(arr)


# (03).Create an array containing 5 zeros using NumPy.

import numpy as np
print(np.zeros(5))

# (04).Create a matrix of zeros having 2 rows and 4 columns.

import numpy as np
matrix=np.zeros((2,4))
print(matrix)

# (05).Create an array containing 6 ones.

import numpy as np
print(np.ones(6))

# (06). Create a 3×3 matrix filled with the value 9.

import numpy as np
print(np.full([3,3],[9]))

#(07). Create an array of even numbers from 0 to 20 using arange().

import numpy as np
print(np.arange(0,20,2)) # it also  consists of Start,stop,step

# (08).Create 6 equally spaced values between 0 and 1.

import numpy as np
v=np.linspace(1,4,5)
print(v)

# (09).Create a 5×5 identity matrix using NumPy.

# by using the eye() function we can make the identity matrix

import numpy as np
matrix=np.eye(3,3)
print(matrix)

# (10).Create a 3×3 matrix containing random integers between 1 and 20.

import numpy as np
matrix=np.random.randint(1,20,size=(3,3))
print(matrix)
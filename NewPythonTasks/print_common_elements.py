# Take two arrays of same size from user and print all the common elements between them.
# For ex - arr1 -> [1 , 2, 3] and arr2 -> [1, 3, 4] -> common element is [1], there can be  multiple elements.
# Condition provided, array provided by the user must be in ascending order (you do not have to sort).

from array import *

arr1 = array('i',[1,5,8,6,0,4,95])
arr2 = array('i',[5,3,7,6,1,0])

for x in arr1:
    if x in arr2:
        print(x, end= ' ')
# Write a python program to insert an element (specific position) into an array.
# for ex-> [1 , 2, 3, 4] insert 6 at index 3 -> [1 , 2 , 3 , 6 , 4]

from array import *

arr = array('i',[1 , 2 , 3 , 6 , 4])

arr.insert(2, 10)
print(arr)

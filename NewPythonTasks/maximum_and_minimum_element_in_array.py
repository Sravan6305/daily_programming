# Find the maximum element in array.
# Find the minimum element in array.

from array import *

arr = array('i',[1,2,3,4,5])
max_arr = 2
min_arr = 2
for x in arr:
    if x > max_arr:
        max_arr = x
    elif x < min_arr:
        min_arr = x
print(max_arr)
print(min_arr)
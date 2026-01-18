# Find position of maximum element in array.
# Find position of minimum element in array.

from array import *

arr = array('i',[5,2,9,1,0,3])
max_arr = 2
min_arr = 9

for x in arr:
    if x > max_arr:
        max_arr = x
    elif x < min_arr:
        min_arr = x
print(max_arr)
print(min_arr)
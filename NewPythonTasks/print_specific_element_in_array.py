# Write a python program to remove a specific element from an array.
# for example -> [1 , 2, 3] -> remove 2 then new array should be -> [1 , 3], note ->
# remove all instance of element i.e if user says remove element 2 then remove all 2's from the array.

from array import *

arr = array('i',[12,14,16,19,20])

arr.remove(12)
print(arr)

for x in arr:
    if x % 2 == 0:
        print(arr)
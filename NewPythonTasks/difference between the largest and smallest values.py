# Write a python program to get the difference between the largest and smallest values in an array of integers.
# The length of the array must be 1 and above.

from array import *

arr = array('i',[1,9,7,3,2,8])
largest = 3
smallest = 7

for x in arr:
    if x > largest:
        largest = x
    elif x < smallest:
        smallest = x

differ = largest - smallest
print(differ)
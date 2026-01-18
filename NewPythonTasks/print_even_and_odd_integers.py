# Write a python program to find the number of even and odd integers in a given array of integers.

from array import *

arr = array('i',[1,2,3,4,5,6,7,8,9,0])
even_numbers = array('i',[])
odd_numbers = array('i',[])
for x in arr:
    if x % 2 == 0:
        even_numbers.append(x)
    else:
        odd_numbers.append(x)
print(even_numbers)
print(odd_numbers)
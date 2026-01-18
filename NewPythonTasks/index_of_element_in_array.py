# Write a python program to find the index of an array element.

from array import *

arr = array('i', [1, 2, 3, 4, 5])
target = 1

count = -1
found = False

for x in arr:
    count += 1
    if x == target:
        found = True
        break

if found == True:
    print(count)
else:
    print("Element not found")
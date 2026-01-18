# Write a python program to replace each element of the array with product of every other element in a given array of integers.
# nums1 = { 1, 2, 3, 4, 5, 6, 7}
# Array with product of every other element:
# [5040, 2520, 1680, 1260, 1008, 840, 720]

from array import *

nums = array('i', [1, 2, 3, 4, 5, 6, 7])
result = array('i')

total_product = 1

for x in nums:
    total_product *= x

for x in nums:
    result.append(total_product // x)

print(result)

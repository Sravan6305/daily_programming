# Write a python program to compute the average value of an array of integers except the largest and smallest values.

from array import *

arr = array('i',[56,78,23,49,18])
max = 23
min = 49
for x in arr:
    if x > max:
        max = x
    elif x < min:
        min = x
arr.remove(max)
arr.remove(min)
sum = sum(arr)
average = sum / len(arr)
print(average)
# Write a Java program that checks an array is negative dominant or not.
# If the array is negative dominant print true otherwise false.
# Original array of numbers:
# [1, -2, -5, -4, 3, -6]
# Check Negative Dominance in the said array! true

from array import *

arr = array('i',[1, -2, -5, -4, 3, -6,0])
positive_count = 0
negative_count = 0
for x in arr:
    if x < 0:
        negative_count += 1
    elif x > 0:
        positive_count += 1

if positive_count < negative_count:
    print('array is negative dominant')
elif positive_count > negative_count:
    print('array is not negative dominance')
# Write a python program to check if the sum of all the 10's in the array is exactly 30.
# Return false if the condition does not satisfy, otherwise true.

from array import *

arr = array('i',[20,40,42,96,10,52,55])
sum = 0
for x in arr:
    if x % 10 == 0:
        sum = sum + x

if sum == 30:
    print('true')
else:
    print('false')
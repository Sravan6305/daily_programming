# Write a python program to check if an array of integers contains two specified elements 65 and 77.

from array import *

arr = array('i',[65,54,89,77,23,15])

for x in arr:
    if x == 65 and x == 77:
        print('both the numbers existed')
    elif x == 65:
        print('only 65 existed')
    elif x == 77:
        print('only 77 existed')
    else:
        print('both elements do not exist')
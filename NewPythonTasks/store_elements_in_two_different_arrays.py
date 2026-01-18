# Take an array of 10 elements.
# Split it into middle and store the elements in two different arrays, and print the prefix sum of both the arrays.

from array import *

arr = array('i',[1,2,3,4,5,6,7,8,9,10])

new_arr1 = array('i',[])
new_arr2 = array('i',[])
sum1 = 0
sum2 = 0
for x in arr[5:]:
    sum1 += x
    new_arr1.append(x)
print(sum1)
print(new_arr1)

for x in arr[:5]:
    sum2 += x
    new_arr2.append(x)
print(sum2)
print(new_arr2)
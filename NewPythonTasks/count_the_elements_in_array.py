# Print the count of all elements in array. [ 1 , 2 , 2 , 2 , 3 , 3 , 3 , 3 , 3 ]
# 1 appears 1 time
# 2 appears 3 times
# 3 appears 5 times

from array import *

arr = array('i',[1, 2, 2, 2, 3, 3, 3, 3, 3])
count1 = 0
count2 = 0
count3 = 0

for x in arr:
    if x == 1:
        count1 = count1 + 1
    elif x == 2:
        count2 = count2 + 1
    elif x == 3:
        count3 = count3 + 1
print(count3)
print(count1)
print(count2)

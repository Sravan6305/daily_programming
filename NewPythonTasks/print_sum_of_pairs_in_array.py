# WAP in python to print the sum of all pairs in array.
# Extra condition last and first element will also be considered. for ex -> [1 , 2 , 3 ,4] -> [3 , 5 , 7 , 5]
# explanation -> 1 + 2 gives 3 , 2 + 3 gives 5 , 3 + 4 gives 7 , 4 + 1 gives 5.

from array import *

arr = array('i', [1, 2, 3, 4])
result = array('i')

n = len(arr)

for i in range(n):
    if i == n - 1:
        result.append(arr[i] + arr[0])
    else:
        result.append(arr[i] + arr[i + 1])

print(result)

# Find sum of squares and sum of cubes of all numbers in array. For ex- [1 , 2 , 3] -> sum of sq -> 1*1 + 2*2 + 3*3 -> sum of cubes -> 1*1*1 + 2*2*2 + 3*3*3

from array import *

arr = array('i', [5, 3, 2, 8])

squares_sum = sum(x ** 2 for x in arr)
cubes_sum = sum(x ** 3 for x in arr)

print(f"Sum of squares: {squares_sum}")
print(f"Sum of cubes: {cubes_sum}")
# When preparing a tournament, Yudhish tries his best to make the first problem as easy as possible.
# This time he has chosen some problem and asked n people about their opinions.
# Each person answered whether this problem is easy or hard.
# If at least one of these n people has answered that the problem is hard, Yudhish gives extra 50 questions to solve.
# For the given responses, check if the problem is easy enough.
# The array will contain only 0's and 1's where 0 means ith person says it is easy ,
# 1 means ith person says it is hard, If any of them says it is hard print "HARD" else print "EASY".

from array import *

arr = array('i', [1, 1, 0, 1, 0, 0, 1, 1])

result = "EASY"

for x in arr:
    if x == 1:
        result = "HARD"
        break

print(result)

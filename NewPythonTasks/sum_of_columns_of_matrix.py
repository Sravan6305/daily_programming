# Find sum of all cols in (n * m) matrix and print the maximum and minimum sum.
# 1 2 3
# 4 2 4
# 1 9 2
# sum of col1 -> 6
# sum of col2 -> 13
# sum of col3 -> 9
# maximum is 13 and minimum is 6

matrix = [[1,2,3], [4,2,4], [1,9,2]]

col1 = matrix[0][0] + matrix[1][0] + matrix[2][0]
col2 = matrix[0][1] + matrix[1][1] + matrix[2][1]
col3 = matrix[0][2] + matrix[1][2] + matrix[2][2]

print(f"sum of col1 is {col1}")
print(f"sum of col2 is {col2}")
print(f"sum of col3 is {col3}")

if col1 > col2 and col1 > col3:
    print("sum of col1 is maximum and minimum is", min(col2, col3))
elif col2 > col1 and col2 > col3:
    print("sum of col2 is maximum and minimum is", min(col1, col3))
elif col3 > col1 and col3 > col2:
    print("sum of col2 is maximum and minimum is", min(col1, col2))



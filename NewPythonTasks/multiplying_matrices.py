# Take two n * n matrix from user and add them.
# for ex:
# let n be 2
# matrix 1:
# 1 2
# 3 4
# matrix 2:
# 1 2
# 3 4
# result matrix:
# 2 4
# 6 8

n = int(input("Enter size of matrix: "))

matrix1 = []
matrix2 = []

print("Enter elements of Matrix 1:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix1.append(row)

print("Enter elements of Matrix 2:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix2.append(row)

result = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Result Matrix:")
for row in result:
    print(row)

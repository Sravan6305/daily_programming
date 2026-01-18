# Find the factorial of a given number. factorial of 5 is -> 5 * 4 * 3 * 2 * 1 -> 120.

def factorial(num):
    product = 1
    for x in range(1, num+1):
        product = product * x

    return product

print(factorial(4))
print(factorial(14))
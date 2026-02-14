# List Number Report
# Given a list:
# [12, 5, 8, 21, 30]
# Function should return:
# sum of list, largest number, smallest number ,even count, odd count


def number_report(numbers):
    total = 0
    largest = numbers[0]
    smallest = numbers[0]
    even_count = 0
    odd_count = 0

    for x in numbers:
        total = total + x
        if x > largest:
            largest = x
        if x < smallest:
            smallest = x

        if x % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    return total, largest, smallest, even_count, odd_count
numbers = [12, 5, 8, 21, 30]
print(number_report(numbers))

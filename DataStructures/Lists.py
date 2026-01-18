# TASK 1: Even–Odd Organizer
# Take 10 numbers from the user. Store them in a list. Create two new lists: one for even numbers and  one for odd numbers
# Print all three lists

# n = int(input('enter the number(1 to n): '))
# number = []
# even_number = []
# odd_number = []
#
# for x in range(1, n+1):
#     number.append(x)
#     if x % 2 == 0:
#         even_number.append(x)
#     else:
#         odd_number.append(x)
# print(number)
# print(even_number)
# print(odd_number)


# TASK 2: Duplicate & Unique Splitter
# Take a list of numbers from the user
# Create: a list of duplicate elements, a list of unique elements
# Print both lists


# numbers = [1, 2, 8, 6, 6, 4]
#
# unique_elements = []
# duplicate_elements = []
#
# for x in numbers:
#     if numbers.count(x) == 1:
#         unique_elements.append(x)
#     elif x not in duplicate_elements:
#         duplicate_elements.append(x)
#
# print(unique_elements)
# print(duplicate_elements)


# TASK 3: Word Length Mapper
# Take a sentence from the user. Convert it into a list of words
# Create a new list that stores: each word along with its length
# print the final list

# sentence = "hello python"
# words = sentence.split()
#
# word_length = []
#
# for x in words:
#     word_length.append((x, len(x)))
#
# print(word_length)


# TASK 4:Given a list of numbers, create a new list where you multiply each number by 2 only if it’s divisible by 3. Print the new list.

# numbers = [3,6,9,8,5,1,2]
# new_list = []
# for x in numbers:
#     if x % 3 == 0:
#         new_list.append(x*2)
# print(new_list)
# Given an array of integers sorted in ascending order, find the starting and ending position of a given value.

# def sort_ascending(list1):
#     for x in range(len(list1)-1):
#         if list1[x] > list1[x+1]:
#             c = list1[x]
#             list1[x] = list1[x+1]
#             list1[x+1] = c
#             x = 0
#     return list1
# print(sort_ascending([5,6,1,8,9,0]))


def sort_ascending(list1):
    x = 0
    while x < len(list1) - 1:
        if list1[x] > list1[x + 1]:
            c = list1[x]
            list1[x] = list1[x + 1]
            list1[x + 1] = c
            x = 0
        else:
            x += 1
    return list1

print(sort_ascending([5, 6, 1, 8, 9, 0]))

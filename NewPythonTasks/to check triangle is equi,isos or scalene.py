# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

l1 = int(input("Enter first side: "))
l2 = int(input("Enter second side: "))
l3 = int(input("Enter third side: "))

if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
    print("Not a valid triangle")
elif l1 == l2 == l3:
    print("It is an equilateral triangle")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("It is an isosceles triangle")
else:
    print("It is a scalene triangle")

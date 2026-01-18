# Write a program in python to input 5 numbers from keyboard and find their sum and average.

def calculate_sum_and_average(a,b,c,d,e):
    sum = a+b+c+d+e
    average = sum / 5
    return sum, average
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
print(calculate_sum_and_average(a,b,c,d,e))

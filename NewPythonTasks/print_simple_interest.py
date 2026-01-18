# WAP to find the simple interest. PRT all three will be user input.

principal = int(input('enter the principal: '))
Rate_of_interest = int(input('enter the Rate_of_interest: '))
time = float(input('enter the time: '))
simple_interest = principal * Rate_of_interest * time / 100
print(simple_interest)
# Write a program to calculate profit or loss. cp and sp provided by user.

cost_price = int(input('enter the price: '))
selling_price = int(input('enter the selling price: '))

if cost_price > selling_price:
    print('loss')
else:
    print('profit')
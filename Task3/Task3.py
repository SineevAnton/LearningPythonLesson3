# Create an array of real numbers. Write a program,
# which will find the difference between max and min values of fractional parts of elements.

import random as rnd

lenArr = int(input('Please enter the length of array: '))
arr = [round(rnd.randint(1, 10) * rnd.random(), 2) for _ in range(lenArr)]
fractionalArr = [round(el % 1, 2) for el in arr]
print(f'Initial array is: {arr}')
print(f'Array of fraction parts: {fractionalArr}')
print(f'Difference etween max {round(max(fractionalArr), 2)} and min {round(min(fractionalArr), 2)} is: {round(max(fractionalArr) - min(fractionalArr), 2)}')
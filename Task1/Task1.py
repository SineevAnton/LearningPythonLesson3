# Create an array of nu,bers. Write a program
# which will find the sum of all elements, placed on odd indexes.

import random as rnd

lenArr = int(input('Please enter the length of array: '))
elementSum = 0
arr = [rnd.randint(1, 10) for _ in range(lenArr)]
for i in range(1, len(arr), 2):
    elementSum += arr[i]
print(f'Initial array: {arr}')
print(f'Summa of elements in odd positions: {elementSum}')
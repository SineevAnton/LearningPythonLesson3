# Write a program which will find the product of numbers pairs.
# The pair is first and last elements, second and penultimate etc.

import random as rnd

lenArr = int(input('Please enter the length of array: '))
elementsProd = []
arr = [rnd.randint(1, 10) for _ in range(lenArr)]
loopRange = len(arr)//2 if len(arr) % 2 == 0 else len(arr)//2 + 1

for i in range(0, loopRange):
    elementsProd.append(arr[i] * arr[-(i+1)])
print(f'Initial array is: {arr}')
print(f'Prods of elements: {elementsProd}')
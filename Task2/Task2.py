# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random as rnd

lenArr = int(input('Please enter the length of array: '))
elementsProd = []
arr = [rnd.randint(1, 10) for _ in range(lenArr)]
loopRange = len(arr)//2 if len(arr) % 2 == 0 else len(arr)//2 + 1

for i in range(0, loopRange):
    elementsProd.append(arr[i] * arr[-(i+1)])
print(f'Initial array is: {arr}')
print(f'Prods of elements: {elementsProd}')
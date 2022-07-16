# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random as rnd

lenArr = int(input('Please enter the length of array: '))
elementSum = 0
arr = [rnd.randint(1, 10) for _ in range(lenArr)]
for i in range(1, len(arr), 2):
    elementSum += arr[i]
print(f'Initial array: {arr}')
print(f'Summa of elements in odd positions: {elementSum}')
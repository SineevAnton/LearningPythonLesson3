# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('Please enter a number: '))
result = ''
while num != 0:
    result += str(num % 2)
    num //= 2
print(f'Binary notation is: {int(result[::-1])}')
def fib(n):
    a, b = 1, 1
    for x in range(n):
        yield a
        a, b = b, a + b
n = int(input('Введите количество чисел Фибоначчи, которые нужно сгенерировать:'))
for number in fib(n):
    print(number)
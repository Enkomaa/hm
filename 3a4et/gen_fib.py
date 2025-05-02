def fibonacci(n):
    current, next = 0, 1  # текущее и следующее числа Фибоначчи
    for _ in range(n):
        yield current
        current, next = next, current + next

for num in fibonacci(6):
    print(num)
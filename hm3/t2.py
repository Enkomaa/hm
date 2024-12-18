def power(a, n):
    if n == 0:
        return 1
    return a * a**(n-1)
print(power(float(input('Введите число a:' )), int(input('Введите число n:'))))
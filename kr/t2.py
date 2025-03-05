a = int(input('Количество информатиков = '))
b = int(input('Количество биологов = '))

def nok(a, b):
    p = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    nod = a + b
    nok = p // nod
    return nok

print(f'Минимальное подходящее число кусочков торта {nok(a, b)}')


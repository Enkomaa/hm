def count_strings_without_ab(n):
    a = [0] * (n + 1)
    b = [0] * (n + 1)

    a[1] = 1  # "a"
    b[1] = 1  # "b"

    for i in range(2, n + 1):
        a[i] = a[i - 1] + b[i - 1]  # cтроки, заканчивающиеся на 'a'
        b[i] = b[i - 1]              # cтроки, заканчивающиеся на 'b'

    total = a[n] + b[n]
    return total

length = 6
result = count_strings_without_ab(length)
print(f"Количество строк длины {length}, не содержащих подстроку 'ab': {result}")
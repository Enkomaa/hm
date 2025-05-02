def count_digits(number_str):
    counts = {}
    for digit in number_str:
        if digit in counts:
            counts[digit] += 1  # если цифра уже есть — увеличиваем счётчик
        else:
            counts[digit] = 1  # если цифры ещё нет — создаём счётчик и ставим 1
    return counts

number_str = input("Введите число: ")
counts = count_digits(number_str)
for digit in sorted(counts):
    print("Цифра", digit, "встречается", counts[digit], "раз")

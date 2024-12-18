def unique_letter_generator(s):
    meet = set()  # множество для уже встреченных букв
    for char in s:
        if char.isalpha() and char not in meet:
            meet.add(char)  # добавляем букву в множество
            yield char  # возвращаем букву

string = input('Введите строку:')
unique_letters = unique_letter_generator(string)

for letter in unique_letters:
    print(letter)
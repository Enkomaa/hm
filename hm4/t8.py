def long_string_generator(strings):
    for string in strings:
        if len(string) > 3:
            yield string

strings = ["cat", "кошка", "dog", "собака", "tea", "чай"]
long_strings = long_string_generator(strings)

for long_string in long_strings:
    print(long_string)
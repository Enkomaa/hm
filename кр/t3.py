def is_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    if even_numbers:
        return even_numbers
    else:
        return "Чётные числа не найдены"

input_array = input("Введите массив чисел через пробел: ").split()
input_array = [int(num) for num in input_array]

result = is_even_numbers(input_array)
print(result)

def sqrt_generator():
    while True:
        number = yield
        if number is not None and number >= 0:
            yield math.sqrt(number)

gen = sqrt_generator()
next(gen)

numbers = [4, 9, -1, 16, -25, 25]
for num in numbers:
    result = gen.send(num)
    if result is not None:
        print(f"Квадратный корень из {num} = {result}")
    else:
        print(f"{num} - отрицательное число")
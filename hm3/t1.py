def distance(x1, y1, x2, y2):
    return ((x2-x1) ** 2 + (y2-y1) ** 2) ** (1/2)
print(distance(int(input('Введите x1:')), int(input('Введите y1:')), int(input('Введите x2:')), int(input('Введите y2:'))))
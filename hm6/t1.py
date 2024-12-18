import re
import matplotlib.pyplot as plt

file_path = '../data.txt'

dates = []
temperatures = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # извлечение даты и температуры
        match = re.search(r'(\d{4}-\d{2}-\d{2}): Temperature = (\d+)°C', line)
        #Задача 3: Фильтрация данных
        if match:
            date = match.group(1)  # Первая группа — дата
            temp = int(match.group(2))  # Вторая группа — температура
            # Фильтрация: добавляем только если температура >= 13°C
            if temp >= 13:
                dates.append(date)
                temperatures.append(temp)
#Задача 1: Анализ максимальной температуры
# Поиск максимальной температуры и соответствующей даты
max_temp = max(temperatures)
max_temp_index = temperatures.index(max_temp)
max_temp_date = dates[max_temp_index]

# Вывод даты с самой высокой температурой
print(f"Дата с самой высокой температурой: {max_temp_date} с температурой {max_temp}°C")

plt.figure(figsize=(10, 6))
plt.plot(dates, temperatures, marker='o', linestyle='-', color='b', label='Temperature')
plt.title('Температура по дням', fontsize=16)
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Температура (°C)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig('temperature_plot.png')
plt.show()
#Задача 2: Гистограмма температур
# Создание гистограммы температур
plt.figure(figsize=(10, 6))
plt.hist(temperatures, bins=10, color='orange', edgecolor='black')  # 10 - количество корзин
plt.title('Гистограмма температур', fontsize=16)
plt.xlabel('Температура (°C)', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.grid(axis='y')
plt.tight_layout()

plt.savefig('temperature_histogram.png')
plt.show()
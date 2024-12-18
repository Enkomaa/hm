import re
import matplotlib.pyplot as plt
from collections import Counter

file_name = "../data_test.txt"

# 1. Подсчет количества транзакций (не включая заголовок)
with open(file_name, "r", encoding="utf-8") as file:
    lines = file.readlines()

transaction_count = len(lines) - 1
print(f"Количество транзакций: {transaction_count}")

# 2. Нахождение общей суммы всех покупок
total_amount = 0.0
for line in lines[1:]:
    parts = line.strip().split(", ")
    amount = float(parts[3])
    total_amount += amount

print(f"Общая сумма всех покупок: ${total_amount:.2f}")

# 3. Извлечение строк, где категория товара — Electronics
electronics_transactions = []
for line in lines[1:]:
    if re.search(r', Electronics,', line):
        electronics_transactions.append(line.strip())

print("Транзакции в категории 'Electronics':")
for transaction in electronics_transactions:
    print(transaction)

# 4. Нахождение транзакций, где сумма больше 100 долларов
high_value_transactions = []
for line in lines[1:]:
    parts = line.strip().split(", ")
    amount = float(parts[3])
    if amount > 100:
        high_value_transactions.append(line.strip())

print("Транзакции с суммой больше 100 долларов:")
for transaction in high_value_transactions:
    print(transaction)

# 5. Построение гистограммы количества покупок в каждой категории
categories = []
for line in lines[1:]:
    parts = line.strip().split(", ")
    category = parts[4]
    categories.append(category)

category_counts = Counter(categories)

plt.figure(figsize=(10, 6))
plt.bar(category_counts.keys(), category_counts.values(), color='skyblue')
plt.title('Количество покупок в каждой категории', fontsize=16)
plt.xlabel('Категория', fontsize=12)
plt.ylabel('Количество покупок', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()

plt.savefig('category_histogram.png')
plt.show()